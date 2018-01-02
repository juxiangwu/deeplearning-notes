# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

'''
QFile文件流方式操作
'''

f = QFile("temp/data.txt")

if not f.open(QIODevice.ReadOnly | QIODevice.Text):
    print("cannot open file")

txtStream = QTextStream(f)

while not txtStream.atEnd():
    line = txtStream.readLine()
    print(line)

f.close()