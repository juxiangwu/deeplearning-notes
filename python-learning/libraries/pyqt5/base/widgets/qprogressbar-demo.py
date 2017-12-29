# -*- coding: utf-8 -*-
'''
QProgressBar控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
       
        centerWidget = QWidget()

        layout = QHBoxLayout()
        
        progressBar1 = QProgressBar(centerWidget)
        progressBar1.setMinimum(0)
        progressBar1.setMaximum(100)
        progressBar1.setValue(50)
        progressBar1.setOrientation(Qt.Horizontal)
        

        progressBar2 = QProgressBar(centerWidget)
        progressBar2.setMinimum(0)
        progressBar2.setMaximum(100)
        progressBar2.setValue(70)
        progressBar2.setOrientation(Qt.Vertical)

        layout.addWidget(progressBar1)
        layout.addWidget(progressBar2)

        centerWidget.setLayout(layout)

        self.setCentralWidget(centerWidget)

        self.resize(640,480)
        self.setWindowTitle("PyQt5-QProgressBar")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())