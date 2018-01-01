# -*- coding: utf-8 -*-
'''
QFileDialog对话框
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QVBoxLayout()
        
        # 添加控件代码

        openDirButton = QPushButton("Open Directory")
        openDirButton.clicked.connect(self.getDirectory)

        getFileNameButton = QPushButton("Open File")
        getFileNameButton.clicked.connect(self.getFileName)

        getFileNamesButton = QPushButton("Open Files")
        getFileNamesButton.clicked.connect(self.getFileNames)

        saveFileNameButton = QPushButton("Save File")
        saveFileNameButton.clicked.connect(self.saveFile)

        layout.addWidget(openDirButton)
        layout.addWidget(getFileNameButton)
        layout.addWidget(getFileNamesButton)
        layout.addWidget(saveFileNameButton)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QFileDialog")

    def getDirectory(self):
        dirlist = QFileDialog.getExistingDirectory(self,"选择文件夹","C:/")
        qDebug(dirlist)

    def getFileName(self):
        filename,filetype = QFileDialog.getOpenFileName(self,"选择文件","C:/","Text Files(*.txt);;JPEG Files(*.jpeg);;PNG Files(*.png);;GIF File(*.gif);;All Files(*)")
        print(filename,filetype)

    def getFileNames(self):
        filenames,ok = QFileDialog.getOpenFileNames(self,"选择多个文件","C:/","All Files(*.*)")
        print(filenames)

    def saveFile(self):
        filename,ok = QFileDialog.getSaveFileName(self,"保存文件","C:/","All Files(*.*)")
        print(filename)

    

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())