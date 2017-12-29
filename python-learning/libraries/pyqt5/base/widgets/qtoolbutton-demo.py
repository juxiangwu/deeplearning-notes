# -*- coding: utf-8 -*-
'''
QToolButton控件
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
        toolbar = self.addToolBar("File")
        btn1 = QToolButton()
        btn1.setIcon(QIcon("datas/app/resources/images/browser-32x32.png"))
        btn1.clicked.connect(self.browser_action)

        btn2 = QToolButton()
        btn2.setIcon(QIcon("datas/app/resources/images/folder-32x32.png"))
        btn2.clicked.connect(self.folder_action)

        toolbar.addWidget(btn1)
        toolbar.addSeparator()
        toolbar.addWidget(btn2)
        
        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QToolBar")

    def browser_action(self):
        qDebug("browser click")
    
    def folder_action(self):
        qDebug("folder click")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())