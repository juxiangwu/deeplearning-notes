# -*- coding: utf-8 -*-
'''
QComboBox控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.combo = QComboBox()
        self.combo.addItem('A')
        self.combo.addItem('B')
        self.combo.addItem('C')
        self.combo.addItem('D')

        self.combo.currentIndexChanged.connect(self.comboIndexChanged)

        layout = QHBoxLayout()
        layout.addWidget(self.combo)

        self.setLayout(layout)

    def comboIndexChanged(self):
        qDebug("index changed:%d" % (self.combo.currentIndex()))
        

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())