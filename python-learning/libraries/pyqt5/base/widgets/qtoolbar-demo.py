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
        toolbar = self.addToolBar("File")
        act1 = toolbar.addAction(QIcon("datas/app/resources/images/browser-32x32.png"),"Browser")
        act1.triggered.connect(self.browser_action)

        act2 = toolbar.addAction(QIcon("datas/app/resources/images/folder-32x32.png"),"Folder")
        act2.triggered.connect(self.folder_action)


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