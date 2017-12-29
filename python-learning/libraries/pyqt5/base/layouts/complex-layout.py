# -*- coding: utf-8 -*-
'''
复杂布局
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        defalutLayout = QVBoxLayout()
        
        vboxlayout = QVBoxLayout()
        hboxlayout = QHBoxLayout()
        gridlayout = QGridLayout()



        # 添加控件代码
        buttons = []
        for i in range(5):
            buttons.append(QPushButton("Grid Button %d" %(i)))
            vboxlayout.addWidget(QPushButton("VBox Button %d" %(i)))
            hboxlayout.addWidget(QPushButton("HBox Button %d" %(i)))

        gridlayout.addWidget(buttons[0],0,0)
        gridlayout.addWidget(buttons[1],0,1)
        gridlayout.addWidget(buttons[2],1,0,1,2) #跨1行2列
        gridlayout.addWidget(buttons[3],2,0)
        gridlayout.addWidget(buttons[4],2,1)

        defalutLayout.addLayout(vboxlayout)
        defalutLayout.addLayout(gridlayout)
        defalutLayout.addLayout(hboxlayout)

        centerWidget.setLayout(defalutLayout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())