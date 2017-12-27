# -*- coding: utf-8 -*-

from PyQt5.QtCore import QUrl, QObject, pyqtSlot  
from PyQt5.QtGui import QGuiApplication  
from PyQt5.QtQuick import QQuickView  
from PyQt5.QtQml import QQmlEngine,QQmlApplicationEngine

import sys,os

class MyClass(QObject):  
    @pyqtSlot(str)    # 输入参数为str类型  
    def outputString(self, string):  #定义qml调用的函数  
        print(string)  
  
if __name__ == '__main__':
    path = 'main.qml'   # 加载的QML文件
    curdir = os.path.dirname(sys.argv[0])
    qmlfile = os.path.join(curdir,path)

    # Create an instance of the application
    app = QGuiApplication(sys.argv)
    # Create QML engine
    engine = QQmlApplicationEngine()
    # Load the qml file into the engine
    engine.load(QUrl(qmlfile))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())           