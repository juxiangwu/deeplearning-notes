# -*- coding: utf-8 -*-
'''
QColorDialog对话框
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

        self.label = QLabel("Hello,PyQt5")
        self.label.resize(100,100)
        self.button = QPushButton("Select Color")

        self.button.clicked.connect(self.openColorDialog)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QColorDialog")

    def openColorDialog(self):
        color = QColorDialog.getColor(Qt.green,self,"Select Color",QColorDialog.DontUseNativeDialog)
        if(color.isValid()):
           self.label.setText(color.name())
           self.label.setPalette(QPalette(color))
           self.label.setAutoFillBackground(True) 

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())