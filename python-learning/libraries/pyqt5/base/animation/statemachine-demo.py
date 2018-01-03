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

        machine = QStateMachine()
        
        state1 = QState(machine)
        state1.assignProperty(button1,b'geometry',QRect(10,10,100,30))
        machine.setInitialState(state1)

        state2 = QState(machine)
        state1.assignProperty(button1,b'geometry',QRect(250,250,100,30))

        transition1 = state1.addTransition(button1.clicked,state2)
        transition1.addAnimation(QPropertyAnimation(button1,b'geometry'))

        transition2 = state2.addTransition(button1.clicked,state1)
        transition2.addAnimation(QPropertyAnimation(button1,b'geometry'))

        button2 = QPushButton("Start")
        button2.setGeometry(120,10,100,30)
        button2.clicked.connect(lambda :machine.start())

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