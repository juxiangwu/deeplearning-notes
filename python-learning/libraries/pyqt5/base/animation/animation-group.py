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

        button2 = QPushButton("Animation 2")
        animation2 = QPropertyAnimation(button2,b"geometry")
        animation2.setDuration(3000)
        animation2.setStartValue(QRect(130,10,100,30))
        animation2.setEndValue(QRect(200,250,100,30))

        group = QSequentialAnimationGroup()
        group.addAnimation(animation)
        group.addAnimation(animation2)

        button3 = QPushButton("Start")
        button3.setGeometry(120,10,100,30)
        button3.clicked.connect(lambda :group.start())

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())