# -*- coding: utf-8 -*-
'''
属性控件
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

        button1 = QPushButton("Animation")
        button1.setGeometry(10,10,100,30)

        animation = QPropertyAnimation(button1,b"geometry")
        animation.setDuration(3000)
        animation.setStartValue(QRect(10,10,100,30))
        animation.setEndValue(QRect(200,150,100,30))

        easingCurve = QEasingCurve(QEasingCurve.InBack)
        animation.setEasingCurve(easingCurve)

        button2 = QPushButton("Start")
        button2.setGeometry(120,10,100,30)
        button2.clicked.connect(lambda :animation.start())

        layout.addWidget(button1)
        layout.addWidget(button2)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())