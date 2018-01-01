# -*- coding: utf-8 -*-
'''
QTableView控件
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
        model = QStandardItemModel()
        
        model.setHeaderData(0,Qt.Horizontal,"Subject")
        model.setHeaderData(1,Qt.Horizontal,"Description")
        model.setHeaderData(2,Qt.Horizontal,"Date")

        model.setVerticalHeaderItem(0,QStandardItem("1"))
        model.setVerticalHeaderItem(0,QStandardItem("2"))
        model.setVerticalHeaderItem(0,QStandardItem("3"))

        model.setData(model.index(0,0),"Monitor")
        model.setData(model.index(0,1),"LCD 24 inch")
        model.setData(model.index(0,2),"2011-11-04")

        model.setData(model.index(1,0),"Monitor")
        model.setData(model.index(1,1),"LCD 24 inch")
        model.setData(model.index(1,2),"2011-11-04")

        model.setData(model.index(2,0),"Monitor")
        model.setData(model.index(2,1),"LCD 24 inch")
        model.setData(model.index(2,2),"2011-11-04")

        tabelView = QTableView()
        tabelView.setModel(model)

        layout.addWidget(tabelView)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())