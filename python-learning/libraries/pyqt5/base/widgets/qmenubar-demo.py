# -*- coding: utf-8 -*-
'''
QMenuBar控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        menubar = self.menuBar()
        
        m1 = menubar.addMenu("File")
        m1.addAction("Edit")
        m1.addAction("View")
        m1.addAction("Tools")
        
        
       
        m3 = menubar.addMenu("Print")
        m3.addAction("Setup Page")
        m2 = m3.addMenu("Save")

        act1 = m2.addAction("New")
        act2 = m2.addAction("Open")

        act1.setShortcut(Qt.CTRL | Qt.Key_A)
        act1.setToolTip("New Menu")

        act2.setCheckable(True)
        
        #self.setGeometry(300,300,640,480)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QMenuBar")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())