# -*- coding: utf-8 -*-
'''
信号与槽
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class ZeroSignal(QObject):
    atzero = pyqtSignal(int)

class ZeroSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.zeros = 0
        self.valueChanged[int].connect(self.checkZero)
        self.zerosig = ZeroSignal()
        self.zerosig.atzero[int].connect(self.countZero)

    def countZero(self, v):
        if v == 0:
            self.zeros += 1
            print(self.zeros)

    def checkZero(self):
        if self.value() == 0:
            self.zerosig.atzero.emit(self.value())
            



class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        dial = QDial()
        dial.setNotchesVisible(True)
        spin = ZeroSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spin)
        self.setLayout(layout)
        dial.valueChanged.connect(spin.setValue)
        spin.valueChanged.connect(dial.setValue)
        spin.valueChanged.connect(self.emitZero)
        self.setWindowTitle("Sinal and Solt")
        
        self.zerobox = spin 
        self.zerobox.zerosig.atzero[int].connect(self.annouce)

    def emitZero(self, v):
        if v == 0:
            self.zerobox.zerosig.atzero.emit(self.zerobox.zeros)

    def annouce(self, v):
        print("zero count: %d" % v)  # print two times because add ZeroSpinBox emit once

def run():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    run()
