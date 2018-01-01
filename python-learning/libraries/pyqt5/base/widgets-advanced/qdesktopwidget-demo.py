# -*- coding: utf-8 -*-
'''
QDesktopWidget控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Widget(QWidget):
    #__slots__ = ("canvas,slider,pixmap","zoom","px_width","px_height","mm_width","mm_height")
    def __init__(self,parent=None):
        super().__init__()
        self.canvas = QWidget()
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)

        layout = QHBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.slider)
        self.zoom = 1.0
        self.setLayout(layout)

        self.pixmap = QPixmap()
        if not self.pixmap.load("datas/app/resources/images/clock.png"):
            qDebug("cannot load image")
            exit(-1)
        self.slider.valueChanged.connect(self.setZoom)


    def paintEvent(self,event):
        painter = QPainter(self)
        painter.scale(self.zoom,self.zoom)
        painter.drawPixmap(0,0,self.pixmap)

    def setZoom(self,value):
        self.zoom = (50 + value) / 50.0
        pixels = self.pixmap.width()

        desk = QDesktopWidget()
        self.px_width = desk.width()
        self.px_height = desk.height()

        self.mm_width = self.px_width * 17.9
        self.mm_height = self.px_height * 17.9

        self.repaint()


class Form(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码

        widget = Widget()

        layout.addWidget(widget)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())
