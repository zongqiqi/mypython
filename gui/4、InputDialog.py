# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
本实例演示如何使用标准输入框，Qt提供了一个  QInputDialog类，QInputDialog类提供了
一种简单方面的对话框来获得用户的单个输入信息，目前提供了 4种数据类型的输入，可
以是一个字符串，一个 Int类型数据，一个  double类型数据或是一个下拉列表框的条目。
其中包括一个提示标签，一个输入控件。若是调用字符串输入框，则为一个 QLineEdit，若
是调用 Int类型或  double类型，则为一个  QSpinBox，若是调用列表条目输入框，则为一个
QComboBox，还包括一个确定输入(Ok)按钮和一个取消输入(Cancel)按钮。

"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
class InputDlg(QDialog):
    def __init__(self,parent=None):
        super(InputDlg,self).__init__(parent)
        label1 = QLabel(self.tr("姓名"))

        label2 = QLabel(self.tr("性别"))
        label3 = QLabel(self.tr("年龄"))
        label4 = QLabel(self.tr("身高"))
        self.nameLabel = QLabel("TengWei")
        self.nameLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.sexLabel = QLabel(self.tr("男"))
        self.sexLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.ageLabel = QLabel("25")
        self.ageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.statureLabel = QLabel("168")
        self.statureLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        nameButton = QPushButton("...")
        sexButton = QPushButton("...")
        ageButton = QPushButton("...")
        statureButton = QPushButton("...")

        self.connect(nameButton, SIGNAL("clicked()"), self.slotName)
        self.connect(sexButton, SIGNAL("clicked()"), self.slotSex)
        self.connect(ageButton, SIGNAL("clicked()"), self.slotAge)
        self.connect(statureButton, SIGNAL("clicked()"), self.slotStature)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.nameLabel, 0, 1)
        layout.addWidget(nameButton, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.sexLabel, 1, 1)
        layout.addWidget(sexButton, 1, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.ageLabel, 2, 1)
        layout.addWidget(ageButton, 2, 2)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.statureLabel, 3, 1)
        layout.addWidget(statureButton, 3, 2)
        self.setLayout(layout)
        self.setWindowTitle(self.tr("资料收集"))

    def slotName(self):
        name, ok = QInputDialog.getText(self, self.tr("用户名"),
                        self.tr("请输入新的名字:"),
                        QLineEdit.Normal, self.nameLabel.text())
        if ok and (not name.isEmpty()):
            self.nameLabel.setText(name)

    def slotSex(self):
        list = QStringList()###创建一个  QStringList对象，包括两个 QString项，用于标准输入对话框中下拉列表框的条目显示。
        list.append(self.tr("男"))
        list.append(self.tr("女"))
        sex, ok = QInputDialog.getItem(self, self.tr("性别"), self.tr("请选择性别"), list)

        if ok:
            self.sexLabel.setText(sex)

    def slotAge(self):
        age, ok = QInputDialog.getInteger(self, self.tr("年龄"),
                                          self.tr("请输入年龄:"),
                                          int(self.ageLabel.text()), 0, 150)
        if ok:
            self.ageLabel.setText(str(age))

    def slotStature(self):
        stature, ok = QInputDialog.getDouble(self, self.tr("身高"),
                                            self.tr("请输入身高:"),
                                            float(self.statureLabel.text()), 0, 2300.00)
        if ok:
            self.statureLabel.setText(str(stature))
app=QApplication(sys.argv)
form=InputDlg()
form.show()
app.exec_()


"""
QInputDialog的getText()函数原型如下：

(QString, bool ok) QInputDialog.getText (QWidget, QString, QString, QLineEdit.EchoMode mode = QLineEdit.Normal, QString text = QString(),
Qt.WindowFlags flags = 0)
此函数的第一个参数为标准输入对话框的父窗口，第二个参数为标准输入对话框的标题名，第三个参数为标准输入对话框的标签提示，第四个参数 mode指定标准输入对话框中
QLineEdit控件的输入模式，第五个参数  text为标准字符串输入对话框弹出时 QLineEdit控件默认出现的文字，最后一个参数指明标准输入对话框的窗体标识。

QInputDialog的 getItem()函数原型如下：
(QString, bool ok) getItem (QWidget, QString, QString, QStringList, int current = 0, bool editable = True, Qt.WindowFlags flags = 0)
此函数的第一个参数为标准输入对话框的父窗窗口，第二个参数为标准输入对话框的标题名，第三个参数为标准输入对话框的标签提示，第四个参数指定标准
输入对话框中QComboBox控件显示的可选条目，为一个  QStringList对象，第五个参数 current为标准条目选择对话框弹出时 QComboBox控件中默认显示的条目序号，
第六个参数  editable指定QComboBox控件中显示的文字是否可编辑，最后一个参数指明标准输入对话框的窗体标识。

QInputDialog的getInteger()函数原型如下：
(int, bool ok) getInteger (QWidget, QString, QString, int value = 0, int min = -2147483647, int max = 2147483647, int step = 1, Qt.WindowFlags flags = 0)
此函数的第一个参数为标准输入对话框的父窗窗口，第二个参数为标准输入对话框的标题名，第三个参数为标准输入对话框的标签提示，第四个参数 value指定标准输入对话框中
QSpinBox控件默认显示值，第五六个参数指定 QSpinBox控件的数值范围，第七个参数  step指定 QSpinBox控件的步进值。



"""






