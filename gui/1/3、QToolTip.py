# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltip')

        self.setToolTip('This is a <b>QWidget</b> widget')#通过调用 setTooltip() 方法来创建提示，我们使用富文本格式。 QWidget 窗口组件显示提示
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))#设置字体，字号


app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())