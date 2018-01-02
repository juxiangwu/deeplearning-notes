# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

'''
QFile文件流方式写操作
'''

f = QFile("temp/data-w.txt")

if not f.open(QIODevice.WriteOnly | QIODevice.Text):
    print("cannot open file")

txtStream = QTextStream(f)
txtStream.setCodec("UTF-8")
txtStream << "Hello,this is the testing line"

f.close()