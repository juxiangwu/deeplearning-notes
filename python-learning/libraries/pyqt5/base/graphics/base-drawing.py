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

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setPen(Qt.blue)
        painter.drawLine(10,10,100,40)
        painter.drawRect(120,10,80,80)

        rectf = QRectF(230.0,10.0,80.0,80.0)
        painter.drawRoundedRect(rectf,20,20)

        p1 = [QPoint(10,100),QPoint(220,110),QPoint(220,190)]
        painter.drawPolyline(QPolygon(p1))

        p2 = [QPoint(120,110),QPoint(220,110),QPoint(220,190)]
        painter.drawPolygon(QPolygon(p2))

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