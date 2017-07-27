# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
通常在处理长时间任务时需要提供进度条的显示，告诉用户当前任务的进展情况。本实例演
示如何使用进度条

"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class Progess(QDialog):
    def __init__(self, parent=None):
        super(Progess, self).__init__(parent)
        self.setWindowTitle(self.tr("使用进度条"))
        numLabel = QLabel(self.tr("文件数目"))
        self.numLineEdit = QLineEdit("10")
        typeLabel = QLabel(self.tr("显示类型"))
        self.typeComboBox = QComboBox()
        self.typeComboBox.addItem(self.tr("进度条"))
        self.typeComboBox.addItem(self.tr("进度对话框"))

        self.progressBar = QProgressBar()

        startPushButton = QPushButton(self.tr("开始"))

        layout = QGridLayout()
        layout.addWidget(numLabel, 0, 0)
        layout.addWidget(self.numLineEdit, 0, 1)
        layout.addWidget(typeLabel, 1, 0)
        layout.addWidget(self.typeComboBox, 1, 1)
        layout.addWidget(self.progressBar, 2, 0, 1, 2)
        layout.addWidget(startPushButton, 3, 1)
        layout.setMargin(15)
        layout.setSpacing(10)
        self.setLayout(layout)
        self.connect(startPushButton, SIGNAL("clicked()"), self.slotStart)

    def slotStart(self):
        num = int(self.numLineEdit.text())####获得当前需要复制的文件数目，这里对应进度条的总的步进值。
        if self.typeComboBox.currentIndex() == 0:##采用进度条的方式显示进度。
            self.progressBar.setMinimum(0)###决定进度条提示的最小值和最大
            self.progressBar.setMaximum(num)
            for i in range(num):
                self.progressBar.setValue(i)
                QThread.msleep(100)
        elif self.typeComboBox.currentIndex() == 1:###采用进度对话框的方式显示进度。
            progressDialog = QProgressDialog(self)##创建一个进度对话框。
            progressDialog.setWindowModality(Qt.WindowModal)###设置进度对话框采用模态方式进行显示，即显示进度的同时，其他窗口将不响应输入信号。
            progressDialog.setMinimumDuration(5)###设置进度对话框出现等待时间，此处设定为  5秒，默认为 4秒。
            progressDialog.setWindowTitle(self.tr("请等待"))
            progressDialog.setLabelText(self.tr("拷贝..."))###设置进度对话框的窗体标题，显示文字信息以及取消按钮的显示文字。
            progressDialog.setCancelButtonText(self.tr("取消"))
            progressDialog.setRange(0, num)
            for i in range(num):
                progressDialog.setValue(i)
                QThread.msleep(100)
                if progressDialog.wasCanceled():###检测“取消”按钮是否被触发，若触发则退出循环并关闭进度对话框，
                    return
app=QApplication(sys.argv)
progess=Progess()
progess.show()
app.exec_()

"""
Qt提供了两种显示进度条的方式，一种是  QProgressBar，另一种是 QProgressDialog，
QProgressBar类提供了种横向或纵向显示进度条的控件表示方式，用来描述任务的完成情
况。QProgressDialog类提供了一种针对慢速过程的进度对话框表示方式，用于描述任务完
成的进度情况。标准的进度条对话框包括一个进度显示条，一个取消按钮以及一个标签。


"""

