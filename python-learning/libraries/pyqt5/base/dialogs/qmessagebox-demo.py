# -*- coding: utf-8 -*-
'''
消息框
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

        btn1 = QPushButton("Critical对话框")
        btn1.clicked.connect(self.showCriticalMessageBox)

        layout.addWidget(btn1)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QMessageBox")

    def showCriticalMessageBox(self):
        reply = QMessageBox.StandardButton
        reply = QMessageBox.critical(self,"Critical","Hi,Critical",QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)

        if reply == QMessageBox.Abort:
            print("Abord")
        elif  reply == QMessageBox.Retry:
            print("Retry")
        else:
            print("Ignore")
           

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())