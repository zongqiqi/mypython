# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Splash Example")
        edit = QTextEdit()
        edit.setText("Splash Example")
        self.setCentralWidget(edit)

        self.resize(600, 450)
        QThread.sleep(3)

app=QApplication(sys.argv)
splash=QSplashScreen(QPixmap("image/21.png"))
splash.show()
app.processEvents()
window=MainWindow()
window.show()
splash.finish(window)
app.exec_()

