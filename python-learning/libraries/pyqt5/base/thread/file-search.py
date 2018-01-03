import codecs
import html.entities
import re
import sys
from PyQt5.QtCore import (QMutex, QThread,pyqtSignal,Qt)

class Walker(QThread):
    finished = pyqtSignal(bool,int)
    indexed = pyqtSignal(str,int)
    COMMON_WORDS_THRESHOLD = 250
    MIN_WORD_LEN = 3
    MAX_WORD_LEN = 25
    INVALID_FIRST_OR_LAST = frozenset("0123456789_")
    STRIPHTML_RE = re.compile(r"<[^>]*?>", re.IGNORECASE|re.MULTILINE)
    ENTITY_RE = re.compile(r"&(\w+?);|&#(\d+?);")
    SPLIT_RE = re.compile(r"\W+", re.IGNORECASE|re.MULTILINE)

    def __init__(self, index, lock, files, filenamesForWords,
                 commonWords, parent=None):
        super(Walker, self).__init__(parent)
        self.index = index
        self.lock = lock
        self.files = files
        self.filenamesForWords = filenamesForWords
        self.commonWords = commonWords
        self.stopped = False
        self.mutex = QMutex()
        self.completed = False


    def stop(self):
        try:
            self.mutex.lock()
            self.stopped = True
        finally:
            self.mutex.unlock()


    def isStopped(self):
        try:
            self.mutex.lock()
            return self.stopped
        finally:
            self.mutex.unlock()


    def run(self):
        self.processFiles()
        self.stop()
        self.finished.emit(self.completed,self.index)


    def processFiles(self):
        def unichrFromEntity(match):
            text = match.group(match.lastindex)
            if text.isdigit():
                return chr(int(text))
            u = html.entities.name2codepoint.get(text)
            return chr(u) if u is not None else ""

        for fname in self.files:
            if self.isStopped():
                return
            words = set()
            fh = None
            try:
                fh = codecs.open(fname, "r", "UTF8", "ignore")
                text = fh.read()
            except EnvironmentError as e:
                sys.stderr.write("Error: {0}\n".format(e))
                continue
            finally:
                if fh is not None:
                    fh.close()
            if self.isStopped():
                return
            text = self.STRIPHTML_RE.sub("", text)
            text = self.ENTITY_RE.sub(unichrFromEntity, text)
            text = text.lower()
            for word in self.SPLIT_RE.split(text):
                if (self.MIN_WORD_LEN <= len(word) <=
                    self.MAX_WORD_LEN and
                    word[0] not in self.INVALID_FIRST_OR_LAST and
                    word[-1] not in self.INVALID_FIRST_OR_LAST):
                    try:
                        self.lock.lockForRead()
                        new = word not in self.commonWords
                    finally:
                        self.lock.unlock()
                    if new:
                        words.add(word)
            if self.isStopped():
                return
            for word in words:
                try:
                    self.lock.lockForWrite()
                    files = self.filenamesForWords[word]
                    if len(files) > self.COMMON_WORDS_THRESHOLD:
                        del self.filenamesForWords[word]
                        self.commonWords.add(word)
                    else:
                        files.add(str(fname))
                finally:
                    self.lock.unlock()
            self.indexed.emit(fname,self.index)
        self.completed = True

import collections
import os
import sys
from PyQt5.QtCore import (QDir, QReadWriteLock, QMutex,Qt)
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QFrame,
                             QHBoxLayout, QLCDNumber, QLabel, QLineEdit, QListWidget,
                             QPushButton, QVBoxLayout)
#import walker_ans as walker


def isAlive(qobj):
    import sip
    try:
        sip.unwrapinstance(qobj)
    except RuntimeError:
        return False
    return True


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.mutex = QMutex()
        self.fileCount = 0
        self.filenamesForWords = collections.defaultdict(set)
        self.commonWords = set()
        self.lock = QReadWriteLock()
        self.path = QDir.homePath()
        pathLabel = QLabel("Indexing path:")
        self.pathLabel = QLabel()
        self.pathLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        self.pathButton = QPushButton("Set &Path...")
        self.pathButton.setAutoDefault(False)
        findLabel = QLabel("&Find word:")
        self.findEdit = QLineEdit()
        findLabel.setBuddy(self.findEdit)
        commonWordsLabel = QLabel("&Common words:")
        self.commonWordsListWidget = QListWidget()
        commonWordsLabel.setBuddy(self.commonWordsListWidget)
        filesLabel = QLabel("Files containing the &word:")
        self.filesListWidget = QListWidget()
        filesLabel.setBuddy(self.filesListWidget)
        filesIndexedLabel = QLabel("Files indexed")
        self.filesIndexedLCD = QLCDNumber()
        self.filesIndexedLCD.setSegmentStyle(QLCDNumber.Flat)
        wordsIndexedLabel = QLabel("Words indexed")
        self.wordsIndexedLCD = QLCDNumber()
        self.wordsIndexedLCD.setSegmentStyle(QLCDNumber.Flat)
        commonWordsLCDLabel = QLabel("Common words")
        self.commonWordsLCD = QLCDNumber()
        self.commonWordsLCD.setSegmentStyle(QLCDNumber.Flat)
        self.statusLabel = QLabel("Click the 'Set Path' "
                                  "button to start indexing")
        self.statusLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)

        topLayout = QHBoxLayout()
        topLayout.addWidget(pathLabel)
        topLayout.addWidget(self.pathLabel, 1)
        topLayout.addWidget(self.pathButton)
        topLayout.addWidget(findLabel)
        topLayout.addWidget(self.findEdit, 1)
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(filesLabel)
        leftLayout.addWidget(self.filesListWidget)
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(commonWordsLabel)
        rightLayout.addWidget(self.commonWordsListWidget)
        middleLayout = QHBoxLayout()
        middleLayout.addLayout(leftLayout, 1)
        middleLayout.addLayout(rightLayout)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(filesIndexedLabel)
        bottomLayout.addWidget(self.filesIndexedLCD)
        bottomLayout.addWidget(wordsIndexedLabel)
        bottomLayout.addWidget(self.wordsIndexedLCD)
        bottomLayout.addWidget(commonWordsLCDLabel)
        bottomLayout.addWidget(self.commonWordsLCD)
        bottomLayout.addStretch()
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(middleLayout)
        layout.addLayout(bottomLayout)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)

        self.walkers = []
        self.completed = []
        self.pathButton.clicked.connect(self.setPath)
        self.findEdit.returnPressed.connect(self.find)
        self.setWindowTitle("Page Indexer")


    def stopWalkers(self):
        for walker in self.walkers:
            if isAlive(walker) and walker.isRunning():
                walker.stop()
        for walker in self.walkers:
            if isAlive(walker) and walker.isRunning():
                walker.wait()
        self.walkers = []
        self.completed = []


    def setPath(self):
        self.stopWalkers()
        self.pathButton.setEnabled(False)
        path = QFileDialog.getExistingDirectory(self,
                    "Choose a Path to Index", self.path)
        if not path:
            self.statusLabel.setText("Click the 'Set Path' "
                                     "button to start indexing")
            self.pathButton.setEnabled(True)
            return
        self.statusLabel.setText("Scanning directories...")
        QApplication.processEvents() # Needed for Windows
        self.path = QDir.toNativeSeparators(path)
        self.findEdit.setFocus()
        self.pathLabel.setText(self.path)
        self.statusLabel.clear()
        self.filesListWidget.clear()
        self.fileCount = 0
        self.filenamesForWords = collections.defaultdict(set)
        self.commonWords = set()
        nofilesfound = True
        files = []
        index = 0
        for root, dirs, fnames in os.walk(str(self.path)):
            for name in [name for name in fnames
                         if name.endswith((".htm", ".html"))]:
                files.append(os.path.join(root, name))
                if len(files) == 1000:
                    self.processFiles(index, files[:])
                    files = []
                    index += 1
                    nofilesfound = False
        if files:
            self.processFiles(index, files[:])
            nofilesfound = False
        if nofilesfound:
            self.finishedIndexing()
            self.statusLabel.setText(
                    "No HTML files found in the given path")


    def processFiles(self, index, files):
        thread = walker.Walker(index, self.lock, files,
                self.filenamesForWords, self.commonWords, self)
        thread.indexed[str,int].connect(self.indexed)
        thread.finished[bool,int].connect(self.finished)
        thread.finished.connect(thread.deleteLater)
        self.walkers.append(thread)
        self.completed.append(False)
        thread.start()
        thread.wait(300) # Needed for Windows


    def find(self):
        word = str(self.findEdit.text())
        if not word:
            try:
                self.mutex.lock()
                self.statusLabel.setText("Enter a word to find in files")
            finally:
                self.mutex.unlock()
            return
        try:
            self.mutex.lock()
            self.statusLabel.clear()
            self.filesListWidget.clear()
        finally:
            self.mutex.unlock()
        word = word.lower()
        if " " in word:
            word = word.split()[0]
        try:
            self.lock.lockForRead()
            found = word in self.commonWords
        finally:
            self.lock.unlock()
        if found:
            try:
                self.mutex.lock()
                self.statusLabel.setText("Common words like '{0}' "
                        "are not indexed".format(word))
            finally:
                self.mutex.unlock()
            return
        try:
            self.lock.lockForRead()
            files = self.filenamesForWords.get(word, set()).copy()
        finally:
            self.lock.unlock()
        if not files:
            try:
                self.mutex.lock()
                self.statusLabel.setText("No indexed file contains "
                        "the word '{0}'".format(word))
            finally:
                self.mutex.unlock()
            return
        files = [QDir.toNativeSeparators(name) for name in
                 sorted(files, key=str.lower)]
        try:
            self.mutex.lock()
            self.filesListWidget.addItems(files)
            self.statusLabel.setText(
                    "{0} indexed files contain the word '{1}'".format(
                    len(files), word))
        finally:
            self.mutex.unlock()


    def indexed(self, fname, index):
        try:
            self.mutex.lock()
            self.statusLabel.setText(fname)
            self.fileCount += 1
            count = self.fileCount
        finally:
            self.mutex.unlock()
        if count % 25 == 0:
            try:
                self.lock.lockForRead()
                indexedWordCount = len(self.filenamesForWords)
                commonWordCount = len(self.commonWords)
            finally:
                self.lock.unlock()
            try:
                self.mutex.lock()
                self.filesIndexedLCD.display(count)
                self.wordsIndexedLCD.display(indexedWordCount)
                self.commonWordsLCD.display(commonWordCount)
            finally:
                self.mutex.unlock()
        elif count % 101 == 0:
            try:
                self.lock.lockForRead()
                words = self.commonWords.copy()
            finally:
                self.lock.unlock()
            try:
                self.mutex.lock()
                self.commonWordsListWidget.clear()
                self.commonWordsListWidget.addItems(sorted(words))
            finally:
                self.mutex.unlock()


    def finished(self, completed, index):
        done = False
        if self.walkers:
            self.completed[index] = True
            if all(self.completed):
                try:
                    self.mutex.lock()
                    self.statusLabel.setText("Finished")
                    done = True
                finally:
                    self.mutex.unlock()
        else:
            try:
                self.mutex.lock()
                self.statusLabel.setText("Finished")
                done = True
            finally:
                self.mutex.unlock()
        if done:
            self.finishedIndexing()


    def reject(self):
        if not all(self.completed):
            self.stopWalkers()
            self.finishedIndexing()
        else:
            self.accept()


    def closeEvent(self, event=None):
        self.stopWalkers()


    def finishedIndexing(self):
        self.filesIndexedLCD.display(self.fileCount)
        self.wordsIndexedLCD.display(len(self.filenamesForWords))
        self.commonWordsLCD.display(len(self.commonWords))
        self.pathButton.setEnabled(True)
        QApplication.processEvents() # Needed for Windows


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()