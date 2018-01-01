# -*- coding: utf-8 -*-
'''
QDocketWidget控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        #layout = QHBoxLayout()
        
        # 添加控件代码
        dock = QDockWidget("Target")
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        listWidget = QListWidget()
        items = ["A","B","C","D","E"]
        listWidget.addItems(items)

        dock.setWidget(listWidget)
        
        self.addDockWidget(Qt.RightDockWidgetArea,dock)
      
        #centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())