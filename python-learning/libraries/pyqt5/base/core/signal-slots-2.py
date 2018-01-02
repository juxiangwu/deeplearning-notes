# -*- coding: utf-8 -*-
'''
信号与槽
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class ValueChanged(QObject):
    valueChanged = pyqtSignal(int)

class SignalSlot(QObject):
    def __init__(self):
        super().__init__()
        self.__value = 0
        self.valueChanged = ValueChanged()

    @pyqtSlot(int)
    def setValue(self,value):
        self.__value = value
        print("set value:%d" %(value))
        self.valueChanged.valueChanged.emit(value)

def onValueChanged(value):
    print("value = %d" % (value))

if __name__ == "__main__":
    ss = SignalSlot()
    ss.valueChanged.valueChanged[int].connect(onValueChanged)
    ss.setValue(1)
    