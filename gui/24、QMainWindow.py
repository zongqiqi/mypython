# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QMainWindow")
        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        self.createActions()
        self.createMenus()
        self.createToolBars()

    def createActions(self):
        self.fileOpenAction = QAction(QIcon(":/fileopen.png"), self.tr("打开"), self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.setStatusTip(self.tr("打开一个文件"))
        self.connect(self.fileOpenAction, SIGNAL("triggered()"), self.slotOpenFile)

        self.fileNewAction = QAction(QIcon(":/filenew.png"), self.tr("新建"), self)
        self.fileNewAction.setShortcut("Ctrl+N")
        self.fileNewAction.setStatusTip(self.tr("新建一个文件"))
        self.connect(self.fileNewAction, SIGNAL("triggered()"), self.slotNewFile)

        self.fileSaveAction = QAction(QIcon(":/filesave.png"), self.tr("保存"), self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.setStatusTip(self.tr("保存文件"))
        self.connect(self.fileSaveAction, SIGNAL("triggered()"), self.slotSaveFile)

        self.exitAction = QAction(QIcon(":/filequit.png"), self.tr("退出"), self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.setStatusTip(self.tr("退出"))
        self.connect(self.exitAction, SIGNAL("triggered()"), self.close)

        self.cutAction = QAction(QIcon(":/editcut.png"), self.tr("剪切"), self)
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.setStatusTip(self.tr("剪切到粘贴板"))
        self.connect(self.cutAction, SIGNAL("triggered()"), self.text.cut)

        self.copyAction = QAction(QIcon(":/editcopy.png"), self.tr("复制"), self)
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.setStatusTip(self.tr("复制到粘贴板"))
        self.connect(self.copyAction, SIGNAL("triggered()"), self.text.copy)

        self.pasteAction = QAction(QIcon(":/editpaste.png"), self.tr("粘贴"), self)
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.setStatusTip(self.tr("粘贴内容到当前处"))
        self.connect(self.pasteAction, SIGNAL("triggered()"), self.text.paste)

        self.aboutAction = QAction(self.tr("关于"), self)
        self.connect(self.aboutAction, SIGNAL("triggered()"), self.slotAbout)

    def createMenus(self):
        fileMenu = self.menuBar().addMenu(self.tr("文件"))
        fileMenu.addAction(self.fileNewAction)
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.exitAction)

        editMenu = self.menuBar().addMenu(self.tr("编辑"))
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.pasteAction)

        aboutMenu = self.menuBar().addMenu(self.tr("帮助"))
        aboutMenu.addAction(self.aboutAction)

    def createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.fileNewAction)
        fileToolBar.addAction(self.fileOpenAction)
        fileToolBar.addAction(self.fileSaveAction)

        editTool = self.addToolBar("Edit")
        editTool.addAction(self.copyAction)
        editTool.addAction(self.cutAction)
        editTool.addAction(self.pasteAction)

    def slotNewFile(self):
        newWin = MainWindow()
        newWin.show()

    def slotOpenFile(self):
        fileName = QFileDialog.getOpenFileName(self)
        if fileName.isEmpty() == False:
            if self.text.document().isEmpty():
                self.loadFile(fileName)
            else:
                newWin = MainWindow()
                newWin.show()
                newWin.loadFile(fileName)

    def loadFile(self, fileName):
        file = QFile(fileName)
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            textStream = QTextStream(file)
            while textStream.atEnd() == False:
                self.text.append(textStream.readLine())

    def slotSaveFile(self):
        pass

    def slotAbout(self):
        QMessageBox.about("about me", self.tr("这是我们的第一个例子"))
app=QApplication(sys.argv)
main=MainWindow()
main.show()
app.exec_()















