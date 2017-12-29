# -*- coding: utf-8 -*-
'''
QSizeGrip控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class SubWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent,Qt.SubWindow)
        
        sizeGrip = QSizeGrip(parent)
        sizeGrip.setFixedSize(QSize(100,200))
        self.setLayout(QVBoxLayout())
        #self.layout().setMargin(0)
        self.layout().addWidget(QTextEdit())

        sizeGrip.setWindowFlag(Qt.WindowStaysOnTopHint)
        sizeGrip.raise_()

class Widget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)



class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码


        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QSizeGrip")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    w = Widget()
    w.resize(400,300)

    sw = SubWindow(w)
    sw.move(200,180)

    w.show()
    
    sys.exit(app.exec_())