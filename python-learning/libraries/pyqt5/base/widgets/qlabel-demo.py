# -*- coding: utf-8 -*-
'''
QLabel控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)

        label1 = QLabel("Hello,this is the QLabel")
        label2 = QLabel()
        label2.setGeometry(10,70,128,128)
        pix = QPixmap("datas/app/resources/images/clock.png")
        label2.setPixmap(pix)


        layout = QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        self.setLayout(layout)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())