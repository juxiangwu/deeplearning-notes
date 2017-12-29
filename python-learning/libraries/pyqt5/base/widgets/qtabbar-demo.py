# -*- coding: utf-8 -*-
'''
QTabBar控件
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

        tab = QTabBar()
        tab.addTab("Browser")
        tab.addTab("Folder")
        tab.addTab("FTP")

        tab.currentChanged.connect(self.tabChanged)

        layout.addWidget(tab)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QTabBar")

    def tabChanged(self,index):
        qDebug("current tab:%d" %(index))

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())