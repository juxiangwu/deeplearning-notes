# -*- coding: utf-8 -*-
'''
大小改变事件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class PaintWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.image = QImage('datas/app/resources/images/clock.png')

    def paintEvent(self,event):

        painter = QPainter(self) #这里一定要把self传入
        #painter.begain()
        painter.drawLine(80, 100, 650, 500); 
        painter.setPen(Qt.red); 
        painter.drawRect(10, 10, 100, 400); 
        painter.setPen(QPen(Qt.green, 5)); 
        painter.setBrush(Qt.blue); 
        painter.drawEllipse(50, 150, 400, 200); 
        painter.drawPixmap(100,100,QPixmap.fromImage(self.image.scaled(100,100,
                                            Qt.IgnoreAspectRatio,Qt.SmoothTransformation)))
        #painter.end()

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