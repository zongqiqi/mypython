# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\zongqiqi\biandaima\Eric4\workplan\move.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
from PyQt4.QtCore import *
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


i =1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.text = QtGui.QTextBrowser(self.centralWidget)
        self.text.setGeometry(QtCore.QRect(200, 300, 275, 223))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        # self.pushButton.setObjectName(_fromUtf8("pushButton"))
        # self.pushButton.setText(_translate("MainWindow", "move...", None))
        self.timer = QTimer()
        MainWindow.connect(self.timer, SIGNAL("timeout()"), self.showbut)
        self.timer.start(10)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showbut(self):
        global i
        if i < 500:
            i+=1
            self.text.append('ok')
            self.pushButton.setGeometry(QtCore.QRect(i, 100, 175, 23))



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

