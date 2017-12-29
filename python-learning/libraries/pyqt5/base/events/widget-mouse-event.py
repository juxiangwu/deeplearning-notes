# -*- coding: utf-8 -*-
'''
鼠标事件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class PaintWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        
    def mousePressEvent(self,event):
        qDebug("mouse press")
        if(event.button() == Qt.LeftButton):
            qDebug("Left Button Pressed")

        if(event.button() == Qt.RightButton):
            qDebug("Right Button Pressed")
            
        if(event.button() == Qt.MidButton or event.button() == Qt.MiddleButton):
            qDebug("Middle Button Pressed")

    def mouseReleaseEvent(self,event):
        qDebug("mouse release")
    
    def mouseDoubleClickEvent(self,event):
        qDebug("mouse double click")
    def mouseMoveEvent(self,event):
        qDebug("mouse move:x=%d,y=%d" %(event.x(),event.y()))

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