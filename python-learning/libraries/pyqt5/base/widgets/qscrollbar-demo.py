# -*- coding: utf-8 -*-
'''
QScollBar控件
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
        
        # 添加控件代码

        xpos = 10
        ypos = 50

       
        hsb = QScrollBar(centerWidget)
        hsb.setOrientation(Qt.Horizontal)
        hsb.setRange(0,100)
        hsb.setGeometry(xpos,30,20,200)
        lb1 = QLabel(centerWidget)
        lb1.setText("%d" %(hsb.value()))
        lb1.setGeometry(xpos + 2,220,30,30)
        hsb.valueChanged.connect(lambda value:lb1.setText("%d" % value))

        layout.addWidget(hsb)
        layout.addWidget(lb1)


        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QScollBar")

   


if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())