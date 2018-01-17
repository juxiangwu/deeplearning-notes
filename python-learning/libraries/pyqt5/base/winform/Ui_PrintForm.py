# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Develop\DeepLearning\deeplearning-learning\temp\eric6-workspaces\qml-hello\PrintForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from modules import printer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 453)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.contentTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.contentTextEdit.setGeometry(QtCore.QRect(10, 70, 291, 371))
        self.contentTextEdit.setObjectName("contentTextEdit")
        self.printerComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.printerComboBox.setGeometry(QtCore.QRect(330, 80, 191, 22))
        self.printerComboBox.setObjectName("printerComboBox")
        self.getPrinterPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.getPrinterPushButton.setGeometry(QtCore.QRect(530, 80, 75, 23))
        self.getPrinterPushButton.setObjectName("getPrinterPushButton")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.printer = printer.Printer()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.getPrinterPushButton.clicked.connect(self.getPrinters)
        self.pushButton.clicked.connect(self.printDoc)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getPrinterPushButton.setText(_translate("MainWindow", "获取打印机"))
        self.pushButton.setText(_translate("MainWindow", "开始打印"))

    def getPrinters(self):
        printers = self.printer.printerList()
        self.printerComboBox.addItems(printers)

    def printDoc(self):
        doc = self.contentTextEdit.toPlainText()
        if doc == None or doc == '':
            return
        printername = self.printerComboBox.currentText()
        self.printer.printing(printername,doc)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

