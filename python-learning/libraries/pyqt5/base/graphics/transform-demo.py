# -*- coding: utf-8 -*-
'''
绘制基本图元
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Widget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.__image = QImage("datas/app/resources/images/qt-logo.png")
    def paintEvent(self,event):
        painter = QPainter(self)
        pen = QPen(Qt.blue,1,Qt.DashLine)
        painter.setPen(pen)
        painter.drawRect(0,0,100,100)

        transform = QTransform()
        transform.translate(50,50)
        transform.rotate(45)
        transform.scale(0.5,0.5)

        painter.setTransform(transform)
        painter.drawImage(QRect(0,0,100,100),self.__image)


class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码

        w = Widget()

        layout.addWidget(w)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())