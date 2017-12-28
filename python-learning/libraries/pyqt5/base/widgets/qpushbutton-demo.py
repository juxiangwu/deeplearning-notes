# -*- coding: utf-8 -*-
'''
QPushButton按钮
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        button = QPushButton()
        button.setText("Click Me")
        style = "background-image:url(:/images/clock.png);font-weight:600;border:0px;color:white;text-align:center;"
        button.setStyleSheet(style)
        layout = QHBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())