# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
选择左侧列表框不同的选项，右侧则显示所选的窗体
"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class StockDialog(QWidget):
    def __init__(self,parent=None):
        super(StockDialog,self).__init__(parent)
        self.setWindowTitle(self.tr("堆栈窗口"))

        listWidget = QListWidget()### QListWidget控件，并在控件中插入  3个条目，作为选择项。
        listWidget.insertItem(0, self.tr("窗口  1"))
        listWidget.insertItem(1, self.tr("窗口  2"))
        listWidget.insertItem(2, self.tr("窗口  3"))
        label1 = QLabel(self.tr("这是窗口  1!"))###创建  3个 QLabel标签控件，作为堆栈窗口显示的三层窗体。
        label2 = QLabel(self.tr("这是窗口  2!"))
        label3 = QLabel(self.tr("这是窗口  3!"))

        stack = QStackedWidget()###创建一个 QStackedWidget堆栈窗。
        stack.addWidget(label1)###调用  addWidget()方法把前面创建的 3个标签控件依次插入堆栈窗中。
        stack.addWidget(label2)
        stack.addWidget(label3)

        mainLayout = QHBoxLayout(self)###使用  QHBoxLayout对整个对话框进行布局。
        mainLayout.setMargin(5)
        mainLayout.setSpacing(5)
        mainLayout.addWidget(listWidget)
        mainLayout.addWidget(stack, 0, Qt.AlignHCenter)
        mainLayout.setStretchFactor(listWidget, 1)
        mainLayout.setStretchFactor(stack, 3)
        self.connect(listWidget, SIGNAL("currentRowChanged(int)"), stack, SLOT("setCurrentIndex(int)"))

app=QApplication(sys.argv)
main=StockDialog()
main.show()
app.exec_()




