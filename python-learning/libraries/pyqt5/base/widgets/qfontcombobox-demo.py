# -*- coding: utf-8 -*-
'''
QFontComboBox控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.label = QLabel("This is the 字体演示")
        fontComboboxes = []
        for _ in range(5):
            item = QFontComboBox()
            fontComboboxes.append(item)
            item.currentFontChanged.connect(self.fontChanged)
            item.currentIndexChanged.connect(self.fontIndexChanged)

        fontComboboxes[0].setFontFilters(QFontComboBox.AllFonts)
        fontComboboxes[1].setFontFilters(QFontComboBox.ScalableFonts)
        fontComboboxes[2].setFontFilters(QFontComboBox.NonScalableFonts)
        fontComboboxes[3].setFontFilters(QFontComboBox.MonospacedFonts)
        fontComboboxes[4].setFontFilters(QFontComboBox.ProportionalFonts)

        layout = QVBoxLayout()

        ypos = 30
        for i in range(5):
            fontComboboxes[i].setGeometry(10,ypos,300,30)
            ypos += 40
            layout.addWidget(fontComboboxes[i])
        #self.label = QLabel("This is the 字体演示")
        self.label.setGeometry(10,ypos,300,30)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def fontIndexChanged(self,index):
        qDebug("current index is :%d" %(index))

    def fontChanged(self,font):
        qDebug("font changed")
        self.label.setFont(font)
       

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())