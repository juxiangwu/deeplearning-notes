# -*- coding: utf-8 -*-
'''
QFontDialog对话框
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QHBoxLayout()
        
        # 添加控件代码

        self.label = QLabel("Hello,PyQt5")
        self.label.resize(100,100)
        self.button = QPushButton("Select Font")

        self.button.clicked.connect(self.openFontDialog)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QFontDialog")

    def openFontDialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())