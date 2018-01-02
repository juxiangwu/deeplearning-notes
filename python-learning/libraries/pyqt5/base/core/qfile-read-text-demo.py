# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

'''
QFile文件读操作
'''

dataFile = QFile('temp/data.txt')

if not dataFile.open(QIODevice.ReadOnly | QIODevice.Text):
    print("cannot open file")

while not dataFile.atEnd():
    line = dataFile.readLine()
    print(line)

dataFile.close()


