# -*- coding: utf-8 -*-
'''
小票打印
'''
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinterInfo,QPrinter
import sys

class Printer():
    
    #打印机列表
   # @staticmethod
    def printerList(self):
        printer = []
        printerInfo = QPrinterInfo()
        for item in printerInfo.availablePrinters():
            printer.append(item.printerName())
        return printer
    
    #打印任务
   # @staticmethod
    def printing(self,printer, context):
        printerInfo = QPrinterInfo()
        p = QPrinter()
        for item in printerInfo.availablePrinters():
            if printer == item.printerName():
                p = QPrinter(item,QPrinter.PrinterResolution)
        doc = QTextDocument()
        doc.setPlainText(context)
        #p.setPageSize(QPrinter.QPagedPaintDevice.A4)
        #doc.setPageSize(QSizeF(p.logicalDpiX()*(80/25.4),
        #                            p.logicalDpiY()*(297/25.4)))
        # 
        #pagesize = QPrinter.QPagedPaintDevice.A4
        #p.setPageSize(pagesize)
        p.setOutputFormat(QPrinter.NativeFormat)
        doc.print_(p)
        '''
        painter = QPainter(p)
        font = painter.font()
        font.setPixelSize(10)
        painter.setFont(font)
        painter.drawText(0,0,100,100,0,context)
        '''
	

