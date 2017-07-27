# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui
"""
退出确认的messagebox（消息提示框）
"""
class MessageBox(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('message box')

#如果我们关闭 QWidget ，将会产生一个 QCloseEvent 事件，我们需要重新实现 closeEvent() 事件来改变组件的行为。
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())