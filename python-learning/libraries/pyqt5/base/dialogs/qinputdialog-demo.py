# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class InputDialog(QWidget):
    def __init__(self):       
        super(InputDialog,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("项目信息")
        self.setGeometry(400,400,300,260)

        label1=QLabel("项目名称:")
        label2=QLabel("项目类型:")
        label3=QLabel("项目人员:")
        label4=QLabel("项目成本:")
        label5=QLabel("项目介绍:")

        self.nameLable = QLabel("PyQt5")
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.styleLable = QLabel("外包")
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.numberLable = QLabel("40")
        self.numberLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.costLable = QLabel("400.98")
        self.costLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.introductionLable = QLabel("服务外包第三方公司")
        self.introductionLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)

        nameButton=QPushButton("...")
        nameButton.clicked.connect(self.selectName)
        styleButton=QPushButton("...")
        styleButton.clicked.connect(self.selectStyle)
        numberButton=QPushButton("...")
        numberButton.clicked.connect(self.selectNumber)
        costButton=QPushButton("...")
        costButton.clicked.connect(self.selectCost)
        introductionButton=QPushButton("...")
        introductionButton.clicked.connect(self.selectIntroduction)

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        mainLayout.addWidget(self.nameLable,0,1)
        mainLayout.addWidget(nameButton,0,2)
        mainLayout.addWidget(label2,1,0)
        mainLayout.addWidget(self.styleLable,1,1)
        mainLayout.addWidget(styleButton,1,2)
        mainLayout.addWidget(label3,2,0)
        mainLayout.addWidget(self.numberLable,2,1)
        mainLayout.addWidget(numberButton,2,2)
        mainLayout.addWidget(label4,3,0)
        mainLayout.addWidget(self.costLable,3,1)
        mainLayout.addWidget(costButton,3,2)
        mainLayout.addWidget(label5,4,0)
        mainLayout.addWidget(self.introductionLable,4,1)
        mainLayout.addWidget(introductionButton,4,2)

        self.setLayout(mainLayout)



    def selectName(self):
        name,ok = QInputDialog.getText(self,"项目名称","输入项目名称:",
                                       QLineEdit.Normal,self.nameLable.text())
        if ok and (len(name)!=0):
            self.nameLable.setText(name)
    def selectStyle(self):
        list = ["外包","自研"]

        style,ok = QInputDialog.getItem(self,"项目性质","请选择项目性质：",list)
        if ok :
            self.styleLable.setText(style)

    def selectNumber(self):
        number,ok = QInputDialog.getInt(self,"项目成员","请输入项目成员人数：",int(self.numberLable.text()),20,100,2)
        if ok :
            self.numberLable.setText(str(number))

    def selectCost(self):
        cost,ok = QInputDialog.getDouble(self,"项目成本","请输入项目成员人数：",float(self.costLable.text()),100.00,500.00,2)
        if ok :
            self.costLable.setText(str(cost))

    def selectIntroduction(self):
        introduction,ok = QInputDialog.getMultiLineText(self,"项目介绍","介绍：","服务外包第三方公司 \nPython project")
        if ok :
            self.introductionLable.setText(introduction)



if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())