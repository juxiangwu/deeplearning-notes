# -*- coding: utf-8 -*-
'''
QDateEdit控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        date1 = QDate(2017,10,1)
        date2 = QDate.currentDate()
        dateEdit1 = QDateEdit(date1)

        layout = QHBoxLayout()
        layout.addWidget(dateEdit1)

        self.setLayout(layout)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())