# -*- coding: utf-8 -*-
'''
QDataWidgetMapper控件
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    __slots__=("model","typeModel","nameEdit","addressEdit",
                "typeComboBox","mapper","previousButton","nextButton")
    def __init__(self,parent=None):
        super().__init__(parent)
        centerWidget = QWidget()
        layout = QGridLayout()
        
        # 添加控件代码
        
        self.setupModel()

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        
        nameLabel = QLabel("Name")
        self.nameEdit = QLineEdit()
        nameLabel.setBuddy(self.nameEdit)

        addressLabel = QLabel("Address")
        self.addressEdit = QTextEdit()
        addressLabel.setBuddy(self.addressEdit)

        typeLabel = QLabel("Type")
        self.typeComboBox = QComboBox()
        self.typeComboBox.setModel(self.typeModel)

        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.mapper.toNext)
        self.previousButton = QPushButton("Previous")
        self.previousButton.clicked.connect(self.mapper.toPrevious)

        self.typeComboBox.currentIndexChanged.connect(self.updateButton)


        self.mapper.addMapping(self.nameEdit,0)
        self.mapper.addMapping(self.addressEdit,1)
        self.mapper.addMapping(self.typeComboBox,2)

        layout.addWidget(nameLabel,0,0,1,1)
        layout.addWidget(self.nameEdit,0,1,1,1)
        
        layout.addWidget(self.previousButton,0,2,1,1)
        
        layout.addWidget(addressLabel,1,0,1,1)
        layout.addWidget(self.addressEdit,1,1,2,1)
        
        layout.addWidget(self.nextButton,1,2,1,1)
       
        layout.addWidget(typeLabel,3,0,1,1)
        layout.addWidget(self.typeComboBox,3,1,1,1)

        centerWidget.setLayout(layout)
        self.setCentralWidget(centerWidget)
        self.resize(640,480)
        self.setWindowTitle("PyQt5-QDataWidgetMapper")

        self.mapper.toFirst()


    def setupModel(self):
        items = ["Home","Work","Other"]
        self.typeModel = QStringListModel(items)

        self.model = QStandardItemModel(5,3)
        names = ["Alice","Bob","Carol","Donald","Emma"]

        address = ["<qt>123 Main Street <br/>Market Town</qt>",
                    "<qt>PO Box 32 <br/>Mail Handling Service<br/>Service City</qt>",
                    "<qt>The Lighthouse<br/>Big City</qt>",
                    "<qt>47338 Park Avenue<br/>Base Camp<br/>Big Mountain</qt>",
                    "<qt>Research Station<br/>Base Camp<br/>Big Mountain</qt>"]
        types = ["0","1","2","0","2"]

        for row in range(5):
            name = QStandardItem(names[row])
            self.model.setItem(row,0,name)
            addr = QStandardItem(address[row])
            self.model.setItem(row,1,addr)
            itemType = QStandardItem(types[row])
            self.model.setItem(row,2,itemType)

    def updateButton(self,index):
        self.previousButton.setEnabled(index > 0)
        self.nextButton.setEnabled(index < self.model.rowCount() - 1)

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())