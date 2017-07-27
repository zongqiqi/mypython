# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
制作统计软件时经常会使用表格将资料列出，或是通过表格进行资料的设置，在 Qt中可以
使用 QTableWidget实现一个表格。本实例演示如何使用表格，并在表格中嵌入控件。

"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setColumnCount(5)
        self.setRowCount(2)
        self.setItem(0, 0, QTableWidgetItem(self.tr("性别")))
        self.setItem(0, 1, QTableWidgetItem(self.tr("姓名")))
        self.setItem(0, 2, QTableWidgetItem(self.tr("出生日期")))
        self.setItem(0, 3, QTableWidgetItem(self.tr("职业")))
        self.setItem(0, 4, QTableWidgetItem(self.tr("收入")))
        lbp1 = QLabel()###在表格中插入一个  QLabel控件，并设置 QLabel的图形属性。
        lbp1.setPixmap(QPixmap("image/21.png"))
        self.setCellWidget(1, 0, lbp1)
        twi1 = QTableWidgetItem("Tom")###设置表格单元的属性为文本显示。
        self.setItem(1, 1, twi1)
        dte1 = QDateTimeEdit()###在表格中插入一个  QDateTimeEdit控件，该控件可以编辑日期时间，
        dte1.setDateTime(QDateTime.currentDateTime())###setCalendarPopup()方法设置是否弹出日历编辑器。
        dte1.setDisplayFormat("yyyy/mm/dd")
        dte1.setCalendarPopup(True)
        self.setCellWidget(1, 2, dte1)
        cbw = QComboBox()###在表格中插入一个  QComboBox控件，调用 QTableWidget的   setCellWidget()
        cbw.addItem("Worker")
        cbw.addItem("Famer")
        cbw.addItem("Doctor")
        cbw.addItem("Lawyer")
        cbw.addItem("Soldier")
        self.setCellWidget(1, 3, cbw)##函数可在某个指定的表格单元格中插入一个控件，函数的前两个参数用于指定单元格的行，列号。
        sb1 = QSpinBox()###在表格中插入一个  QSpinBox控件。
        sb1.setRange(1000, 10000)
        self.setCellWidget(1, 4, sb1)

app = QApplication(sys.argv)
myqq=MyTable()
myqq.setWindowTitle("My Table")
myqq.show()
app.exec_()





