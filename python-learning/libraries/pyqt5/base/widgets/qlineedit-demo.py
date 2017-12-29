# -*- coding: utf-8 -*-
'''
QLineEdit控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        lineEdit = QLineEdit()
        lineEdit.setStyleSheet("background:yellow;")
        layout = QHBoxLayout()
        layout.addWidget(lineEdit)
        label = QLabel()
        layout.addWidget(label)
        lineEdit.textChanged.connect(label.setText)
        self.setLayout(layout)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())