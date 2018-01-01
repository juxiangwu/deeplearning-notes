# -*- coding: utf-8 -*-
'''
QColumnView控件
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
        name = QStandardItem("Name")
        firstName = QStandardItem("First Name")
        lastName = QStandardItem("Last Name")

        name.appendRow(firstName)
        name.appendRow(lastName)
        model.appendRow(name)

        jhon = QStandardItem("Jhon")
        smith = QStandardItem("Smith")

        firstName.appendRow(jhon)
        lastName.appendRow(smith)

        address = QStandardItem("Address")
        street = QStandardItem("Street")
        city = QStandardItem("City")
        state = QStandardItem("State")
        country = QStandardItem("Country")

        address.appendRow(street)
        address.appendRow(city)
        address.appendRow(state)
        address.appendRow(country)
        model.appendRow(address)

        view = QColumnView()
        view.setModel(model)

        layout.addWidget(view)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-")

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())