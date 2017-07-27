# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
分割窗口是应用程序中经常用到的，它可以灵活分布窗口的布局，经常用于类似文件资源管
理器的窗口设计中

"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        font = QFont(self.tr("黑体"), 12)##指定显示的字体。
        QApplication.setFont(font)

        mainSplitter = QSplitter(Qt.Horizontal, self)###定义一个 QSplitter类对象，为主分割窗口，设定此分割窗为水平分割窜。
        leftText = QTextEdit(self.tr("左窗口"), mainSplitter)###定义一个 QTextEdit类对象，并插入主分割窗口中。
        leftText.setAlignment(Qt.AlignCenter)###调用  setAlignment()方法，设定 TextEdit中文字的对齐方式
        rightSplitter = QSplitter(Qt.Vertical, mainSplitter)
        rightSplitter.setOpaqueResize(False)
        upText = QTextEdit(self.tr("上窗口"), rightSplitter)
        upText.setAlignment(Qt.AlignCenter)
        bottomText = QTextEdit(self.tr("下窗口"), rightSplitter)
        bottomText.setAlignment(Qt.AlignCenter)
        mainSplitter.setStretchFactor(1, 1)
        mainSplitter.setWindowTitle(self.tr("分割窗口"))
        self.setCentralWidget(mainSplitter)

app=QApplication(sys.argv)
main=MainWidget()
main.show()
app.exec_()

"""
setAlignment()方法，设定 TextEdit中文字的对齐方式，常用的有以下几种:
Qt.AlignLeft：左对齐。
Qt.AlignRight：右对齐。
Qt.AlignCenter：文字居中(Qt.AlignHCenter为水平居中，Qt.AlignVCenter为垂直居中)。
Qt.AlignUp：文字与顶端对齐。
Qt.AlignBottom：文字与底部对齐。

"""
