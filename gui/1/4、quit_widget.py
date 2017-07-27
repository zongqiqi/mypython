# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
"""
pushbutton的使用：QPushButton(string text, QWidget parent = None)
参数 text 是显示在按钮上的文本， parent 是放置按钮的父亲，在这里是 QWidget 。
"""
class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        quit = QtGui.QPushButton(u'退出', self)
        quit.setGeometry(10, 10, 64, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())