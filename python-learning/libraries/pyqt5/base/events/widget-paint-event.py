# -*- coding: utf-8 -*-
'''
重写paintEvent
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class PaintWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        
    def resizeEvent(self,event):
        qDebug("[w=%d,height=%d]" % (self.width(),self.height()))

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码

        pw = PaintWidget()
        layout.addWidget(pw)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-PaintEvent")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())