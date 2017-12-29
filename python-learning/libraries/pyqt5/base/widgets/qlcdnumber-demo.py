# -*- coding: utf-8 -*-
'''
QLCDNumber控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        lcd1 = QLCDNumber(2)
        lcd1.display("24")
        lcd2 = QLCDNumber(5)
        lcd2.display("10:30")
        
        layout = QHBoxLayout()
        layout.addWidget(lcd1)
        layout.addWidget(lcd2)
        self.setLayout(layout)
        self.resize(640,480)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())