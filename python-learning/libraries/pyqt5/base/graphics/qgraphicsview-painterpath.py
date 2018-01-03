# -*- coding: utf-8 -*-
'''
视图框架
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    scene = QGraphicsScene()
   
    painterPath = QPainterPath()
    painterPath.moveTo(30,120)
    painterPath.cubicTo(80,0,50,50,80,80)

    scene.addPath(painterPath)

    view = QGraphicsView(scene)
    view.setWindowTitle("PyQt5-QGraphicsView")
    view.resize(640,480)
    view.show()

    app.exec_()