# -*- coding: utf-8 -*-
'''
QToolBox控件
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
        toolbox = QToolBox()
        toolbox.addItem(QLabel("MySQL"),"Database")
        toolbox.addItem(QPushButton("Help"),"Help")
        toolbox.addItem(QLabel("Lily"),"Friends")

        layout.addWidget(toolbox)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QToolBox")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())