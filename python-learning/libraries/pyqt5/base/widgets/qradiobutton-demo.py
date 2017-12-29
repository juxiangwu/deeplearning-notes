# -*- coding: utf-8 -*-
'''
QRadioButton控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        str1 = ["Notebook","Handset","Tablet"]
        str2 = ["In-Vehicle","Smart TV","Media Phone"]

        ypos = 30
        radiobuttons1 = []
        radiobuttons2 = []
        radiogroup1 = QButtonGroup(parent = centerWidget)
        radiogroup2 = QButtonGroup(parent = centerWidget)

        for i in range(3):
            rb = QRadioButton(str1[i],parent=centerWidget)
            rb1 = QRadioButton(str2[i],parent=centerWidget)
            rb.setGeometry(10,ypos,150,30)
            rb1.setGeometry(180,ypos,150,30)
            radiobuttons1.append(rb)
            radiobuttons2.append(rb1)
            ypos += 40
            radiogroup1.addButton(rb)
            radiogroup2.addButton(rb1)

        radiobuttons1[0].setChecked(True)
        radiobuttons2[2].setChecked(True)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QRadioButton")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())