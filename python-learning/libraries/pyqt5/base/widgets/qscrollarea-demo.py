# -*- coding: utf-8 -*-
'''
QScrollArea控件
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
        
        label = QLabel(parent = centerWidget)
        pix = QPixmap('datas/app/resources/images/clock.png')
        label.setPixmap(pix)

        area = QScrollArea(parent = centerWidget)
        area.setWidget(label)
        area.setBackgroundRole(QPalette.Dark)
        area.setGeometry(0,0,pix.width(),pix.height() - 60)

        #layout.addWidget(label)
        layout.addWidget(area)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QScrollArea")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())