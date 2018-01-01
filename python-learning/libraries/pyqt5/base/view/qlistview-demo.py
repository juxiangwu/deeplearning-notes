# -*- coding: utf-8 -*-
'''
控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QVBoxLayout()
        
        # 添加控件代码

        items = ["Monday","Tuesday","Wensday","Thusday","Friday","Statuday","Sunday"]

        model = QStringListModel(items)

        listView = QListView()
        listView.setModel(model)

        index = model.index(3,0)
        text = model.data(index,Qt.DisplayRole)
        
        layout.addWidget(listView)

        label = QLabel()
        label.setText(text)
        layout.addWidget(label)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QListView")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())