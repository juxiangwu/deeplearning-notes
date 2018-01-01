# -*- coding: utf-8 -*-
'''
视图
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
        splitter = QSplitter()
        fsModel = QFileSystemModel()
        fsModel.setRootPath(QDir.currentPath())

        treeView = QTreeView(splitter)
        treeView.setModel(fsModel)
        treeView.setRootIndex(fsModel.index(QDir.currentPath()))

        listView = QListView(splitter)
        listView.setModel(fsModel)
        listView.setRootIndex(fsModel.index(QDir.currentPath()))

        layout.addWidget(splitter)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())