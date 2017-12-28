# -*- coding: utf-8 -*-
'''
QButtonGroup控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        layout=QVBoxLayout()  # layout for the central widget
        widget=QWidget(self)  # central widget
        widget.setLayout(layout)

        number_group=QButtonGroup(widget) # Number group
        r0=QRadioButton("0")
        number_group.addButton(r0)
        r1=QRadioButton("1")
        number_group.addButton(r1)
        layout.addWidget(r0)
        layout.addWidget(r1)

        letter_group=QButtonGroup(widget) # Letter group
        ra=QRadioButton("a")
        letter_group.addButton(ra)
        rb=QRadioButton("b")
        letter_group.addButton(rb)
        layout.addWidget(ra)
        layout.addWidget(rb)

        # assign the widget to the main window
        self.setCentralWidget(widget)



if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())