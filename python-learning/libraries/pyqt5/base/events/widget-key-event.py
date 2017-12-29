# -*- coding: utf-8 -*-
'''
按键事件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class PaintWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.image = QImage('datas/app/resources/images/clock.png')

    def keypressEvent(self,event):
        qDebug("key press")
        if(event.key() == Qt.Key_A):
            qDebug("Key_A press")
    
    def keyreleaseEvent(self,event):
        qDebug("key release")

    def focusInEvent(self,event):
        qDebug("focus in")

    def focusOutEvent(self,event):
        qDebug("focus out")

    
class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码

        pw = PaintWidget()
        layout.addWidget(pw)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-PaintEvent")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())