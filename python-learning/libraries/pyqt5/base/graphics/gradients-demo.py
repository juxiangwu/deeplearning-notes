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

        graident = QLinearGradient(QPointF(70,70),QPointF(140,140))
        graident.setColorAt(0,Qt.blue)
        graident.setColorAt(1,Qt.green)
        graident.setSpread(QGradient.PadSpread)

        brush = QBrush(graident)

        painter.setBrush(brush)

        painter.drawRect(20,20,200,200)

        radg = QRadialGradient(100,100,50,120,120)
        radg.setSpread(QGradient.PadSpread)
        radg.setColorAt(0,Qt.blue)
        radg.setColorAt(1,Qt.green)

        brush = QBrush(radg)
        painter.setBrush(brush)
        painter.drawRect(230,20,200,200)

        cong = QConicalGradient(100,100,45.0)
        cong.setColorAt(0,Qt.blue)
        cong.setColorAt(1,Qt.green)

        brush = QBrush(cong)
        painter.setBrush(brush)
        painter.drawRect(20,210,200,200)

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