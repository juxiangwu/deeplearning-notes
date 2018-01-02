# -*- coding: utf-8 -*-
'''
信号和槽
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        dial = QDial()
        dial.setNotchesVisible(True)
        spinBox = QSpinBox()
        
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinBox)

        self.setLayout(layout)
        #self.connect(dial,SIGNAL("valueChanged(int)"),spinBox.setValue)
        #self.connect(spinbox,SIGNAL("valueChanged(int"),dial.setValue)
        dial.valueChanged.connect(spinBox.setValue)
        spinBox.valueChanged.connect(dial.setValue)

        self.setWindowTitle("Signal and slot")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())