# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
抽屉效果是软件界面设计中的一种常用形式，目前很多流行软件都采用了抽屉效果，如腾讯
公司的 QQ软件，抽屉效果可以以一种动态直观的方式在有限大小的界面上扩展出更多的
功能。


"""
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyQQ(QToolBox):
    def __init__(self, parent=None):
        super(MyQQ, self).__init__(parent)

        toolButton1_1 = QToolButton()###创建了一个 QToolButton类实例，在这里  QToolButton分别对应于抽屉中的每一个
        toolButton1_1.setText(self.tr("朽木"))###对按钮的文字，图标以及大小等进行设置。
        toolButton1_1.setIcon(QIcon("image/21.png"))
        toolButton1_1.setIconSize(QSize(60, 60))
        toolButton1_1.setAutoRaise(True)###设置按钮的  AutoRaise属性为 True，即当鼠标离开时，按钮自动恢复成弹起状态。
        toolButton1_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)###设置按钮的 ToolButtonStyle属性，ToolButtonStyle属性主要用来描述按钮的文字

        toolButton1_2 = QToolButton()
        toolButton1_2.setText(self.tr("Cindy"))
        toolButton1_2.setIcon(QIcon("image/21.png"))
        toolButton1_2.setIconSize(QSize(60, 60))
        toolButton1_2.setAutoRaise(True)
        toolButton1_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton1_3 = QToolButton()
        toolButton1_3.setText(self.tr("了了"))
        toolButton1_3.setIcon(QIcon("image/21.png"))
        toolButton1_3.setIconSize(QSize(60, 60))
        toolButton1_3.setAutoRaise(True)
        toolButton1_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton1_4 = QToolButton()
        toolButton1_4.setText(self.tr("张三虎"))
        toolButton1_4.setIcon(QIcon("image/21.png"))
        toolButton1_4.setIconSize(QSize(60, 60))
        toolButton1_4.setAutoRaise(True)
        toolButton1_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton1_5 = QToolButton()
        toolButton1_5.setText(self.tr("CSDN"))
        toolButton1_5.setIcon(QIcon("image/21.png"))
        toolButton1_5.setIconSize(QSize(60, 60))
        toolButton1_5.setAutoRaise(True)
        toolButton1_5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton2_1 = QToolButton()
        toolButton2_1.setText(self.tr("天的另一边"))
        toolButton2_1.setIcon(QIcon("image/21.png"))
        toolButton2_1.setIconSize(QSize(60, 60))
        toolButton2_1.setAutoRaise(True)
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton2_2 = QToolButton()
        toolButton2_2.setText(self.tr("蓝绿不分"))
        toolButton2_2.setIcon(QIcon("image/21.png"))
        toolButton2_2.setIconSize(QSize(60, 60))
        toolButton2_2.setAutoRaise(True)
        toolButton2_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton3_1 = QToolButton()
        toolButton3_1.setText(self.tr("老牛"))
        toolButton3_1.setIcon(QIcon("image/21.png"))
        toolButton3_1.setIconSize(QSize(60, 60))
        toolButton3_1.setAutoRaise(True)
        toolButton3_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton3_2 = QToolButton()
        toolButton3_2.setText(self.tr("张三疯"))
        toolButton3_2.setIcon(QIcon("image/21.png"))
        toolButton3_2.setIconSize(QSize(60, 60))
        toolButton3_2.setAutoRaise(True)
        toolButton3_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        groupbox1 = QGroupBox()###创建了一个 QGroupBox类实例，在本例中对应每一个抽屉。
        vlayout1 = QVBoxLayout(groupbox1)###创建一个 QVBoxLayout类实例，用来设置抽屉内各按钮的布局。
        vlayout1.setMargin(10)##设置布局中各按钮的显示间距和显示位置。
        vlayout1.setAlignment(Qt.AlignCenter)##设置布局中各按钮的显示间距和显示位置。
        vlayout1.addWidget(toolButton1_1)###将抽屉内的各个按钮加入。
        vlayout1.addWidget(toolButton1_2)
        vlayout1.addWidget(toolButton1_3)
        vlayout1.addWidget(toolButton1_4)
        vlayout1.addWidget(toolButton1_5)
        vlayout1.addStretch()###调用  addStretch()方法在按钮之后插入一个占位符，使得所有按钮能靠上对齐。并
                            ###且在整个抽屉大小发生改变时，保证按钮的大小不发生变化。
        groupbox2 = QGroupBox()
        vlayout2 = QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)
        vlayout2.addWidget(toolButton2_2)

        groupbox3 = QGroupBox()
        vlayout3 = QVBoxLayout(groupbox3)
        vlayout3.setMargin(10)
        vlayout3.setAlignment(Qt.AlignCenter)
        vlayout3.addWidget(toolButton3_1)
        vlayout3.addWidget(toolButton3_2)

        self.addItem(groupbox1, self.tr("我的好友"))###把准备好的抽屉插入至  QToolBox中。
        self.addItem(groupbox2, self.tr("同事"))
        self.addItem(groupbox3, self.tr("黑名单"))

app=QApplication(sys.argv)
myqq = MyQQ()
myqq.setWindowTitle("My QQ")
myqq.show()
app.exec_()


"""
Qt定义了  4种  QToolButtonStyle类型，分别介绍如下:
Qt.ToolButtonIconOnly：只显示图标。
Qt.ToolButtonTextOnly：只显示文字。
Qt.ToolButtonTextBesideIcon：文字显示在图标旁边。
Qt.ToolButtonTextUnderIcon：文字显示在图标下面。
"""













