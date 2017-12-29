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
        #style = "background-image:url(:/images/clock.png);font-weight:600;border:0px;color:white;text-align:center;"
        #button.setStyleSheet(style)
        
        button.clicked.connect(self.btn_clicked)
        button.pressed.connect(self.btn_pressed)
        button.released.connect(self.btn_released)

        focusFrame = QFocusFrame()
        focusFrame.setWidget(button)

        layout = QHBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)
    
    def btn_pressed(self):
        qDebug("button pressed")
    
    def btn_clicked(self):
        qDebug("button click")

    def btn_released(self):
        qDebug("button release")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())