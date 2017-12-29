# -*- coding: utf-8 -*-
'''
QGridLayout垂直布局
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QGridLayout()
        
        # 添加控件代码
        buttons = []
        for i in range(5):
            buttons.append(QPushButton("Button %d" %(i)))
        layout.addWidget(buttons[0],0,0)
        layout.addWidget(buttons[1],0,1)
        layout.addWidget(buttons[2],1,0,1,2) #跨1行2列
        layout.addWidget(buttons[3],2,0)
        layout.addWidget(buttons[4],2,1)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())