# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
"""
和大多数操作系统一样，Windows及  Linux都提供了一系列的标准对话框，如文件选择，
字体选择，颜色选择等，这些标准对话框为应用程序提供了一致的观感。Qt对这些标准对
话框都定义了相关的类，这些类让使用者能够很方便地使用标准对话框进行文件，颜色以及
字体的选择。标准对话框在软件设计过程中是经常需要使用的。

单击“文件对话框”按钮，会弹出文件选择对话框，选中的文件名将显示在右连，
单击“颜色对话框”按钮，会弹出颜色选择对话框，选中的颜色将显示在右边，单击“字体对话
框”按钮，会弹出字体选择对话框，选中的字体将更新右边显示的字符串。


"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))##设定tr方法使用utf8编码来解析文字
class StandardDialog(QDialog):
    def __init__(self,parent=None):
        super(StandardDialog,self).__init__(parent)
        self.setWindowTitle("Standar Dialog")###程序标题

        filePushButton = QPushButton(self.tr("文件对话框"))
        colorPushButton = QPushButton(self.tr("颜色对话框"))###按钮控件
        fontPushButton = QPushButton(self.tr("字体对话框"))

        self.fileLineEdit = QLineEdit()#用来显示文件名的lineedit
        self.colorFrame = QFrame()#显示颜色的qframe,选择不同的颜色时colorFrame会根据用户选择的颜色更新其背景。
        self.colorFrame.setFrameShape(QFrame.Box)
        self.colorFrame.setAutoFillBackground(True)
        self.fontLineEdit = QLineEdit("Hello World")#创建一个 QLineEdit类实例  fontLineEdit，当用户选择不同的字体时，fontLineEdit会根据用户选择的字体更新其内容

        layout = QGridLayout()
        layout.addWidget(filePushButton,0,0)
        layout.addWidget(self.fileLineEdit,0,1)
        layout.addWidget(colorPushButton,1,0)
        layout.addWidget(self.colorFrame,1,1)###将各个控件进行布局。
        layout.addWidget(fontPushButton,2,0)
        layout.addWidget(self.fontLineEdit,2,1)
        self.setLayout(layout)

        self.connect(filePushButton,SIGNAL("clicked()"),self.openFile)
        self.connect(colorPushButton,SIGNAL("clicked()"),self.openColor)###将各个按钮的 clicked信号相应的槽进行连接。
        self.connect(fontPushButton,SIGNAL("clicked()"),self.openFont)
    def openFile(self):###getOpenFileName()是QFileDialog类的一个静态方法，返回用户选择的文件名，如果用户选择取消，则返回一个空串.
        s=QFileDialog.getOpenFileName(self,"Open file dialog","/","Python files(*.py)")
        self.fileLineEdit.setText(str(s))

    def openColor(self):
        c=QColorDialog.getColor(Qt.red)
        if c.isValid():
            self.colorFrame.setPalette(QPalette(c))
    def openFont(self):
        f,ok = QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(f)
app = QApplication(sys.argv)
form=StandardDialog()
form.show()
app.exec_()

"""
getOpenFileName():

QString getOpenFileName (QWidget parent = None, QString caption = QString(), QString
directory = QString(), QString filter = QString(), Options options = 0)
QString getOpenFileName (QWidget parent = None, QString caption = QString(), QString
directory = QString(), QString filter = QString(), QString selectedFilter = None, Options
options = 0)

调用 getOpenFileName()函数将创建一个模态的文件对话框，如下图所示。directory参数
指定了默认的目录，如果 directory参数带有文件名，则该文件将是默认选中的文件，filter
参数对文件类型进行过滤，只有与过滤器匹配的文件类型才显示，filter可以同时指定多种
过滤方式供用户选择，多种过滤器之间用";;"隔开，用户选择的过滤器通过参数  selectedFilter
返回。


QColorDialog:
QColor QColorDialog.getColor (QColor initial = Qt.white, QWidget parent = None)
QColor QColorDialog.getColor (QColor, QWidget, QString, ColorDialogOptions options = 0)

调用 getColor()函数将创建一个模态的颜色对话框，如下图所示。initial参数指定了默认的
颜色，默认为白色，通过 isValid()可以判断用户选择的颜色是否有效，若用户选择取消，
isValid()将返回 false。

QFontDialog:

(QFont, bool) getFont (QFont, QWidget, QString, FontDialogOptions)
(QFont, bool) getFont (QFont, QWidget, QString)
(QFont, bool) getFont (QFont, QWidget parent = None)
(QFont, bool) getFont (QWidget parent = None)

调用 getFont()函数将创建一个模态的字体对话框，如下图所示。用户选择 OK，函数返回(用户选择的字体,True),否则返回(默认字体,False)


"""





