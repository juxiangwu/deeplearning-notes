# -*- coding: utf-8 -*-
'''
控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码
        tab = QTabWidget()

        browser = QWidget()
        folder = QWidget()

        browserLabel = QLabel("Browser")
        browserLayout = QHBoxLayout()
        browserLayout.addWidget(browserLabel)
        browser.setLayout(browserLayout)

        folderLabel = QLabel("Folder")
        folderLayout = QHBoxLayout()
        folderLayout.addWidget(folderLabel)
        folder.setLayout(folderLayout)
        tab.addTab(browser,QIcon("datas/app/resources/images/browser-32x32.png"),"Browser")
        tab.addTab(folder,QIcon("datas/app/resources/images/folder-32x32.png"),"Folder")

        layout.addWidget(tab)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())