# -*- coding: utf-8 -*-

from PyQt4.QtGui import *# 导入  PyQt4.QtGui的所有类及模块，包括 QApplication，所有 Qt图形化应用程序都
from PyQt4.QtCore import *# 必须包含此文件，它包含了 Qt图形化应用程序的各种资源，基本设置，控制流以及事件处
import sys                  # 理等。
"""
本实例实现一个"Hello Kitty!"例子，简单介绍 Qt编程的基本流程，以及  Qt程序的编绎运行
方式

"""
app = QApplication(sys.argv)#创建了一个 QApplication对象，每个 Qt应用程序都必须有且只有一个  QApplication对象，采用 sys.argv作为参数，便于程序处理命令行参数。
b = QPushButton('Hello Kitty')#创建了一个 QPushButton对象，并设置它的显示文本为“Hello Kitty！”，由于此处并没有指定按钮的父窗体，因此以自己作为主窗口。
b.show()#调用  show()方法，显示此按钮。控件被创建时，默认是不显示的，必须调用  show()函数来显示它。
app.connect(b,SIGNAL("clicked()"),app,SLOT("quit()"))#信号与槽的机制,与之相连的 QApplication对象的槽  quit()响应按钮单击信号，执行退出应用程序的操作
app.exec_()#最后调用 QApplication的  exec_()方法，程序进入消息循环


###信号于槽：

###一个信号可以与另一个信号相连：connect(Object1,SIGNAL(signal1),Object2,SIGNAL(signal1))=========即表示 Object1的信号  1发射可以触发 Object2的信号  1发射。
###表示一个信号可以与多个槽相连：connect(Object1,SIGNAL(signal2),Object2,SLOT(slot2)) ==========connect(Object1,SIGNAL(signal2),Object3,SLOT(slot1))
###表示同一个槽可以响应多个信号：connect(Object1,SIGNAL(signal2),Object2,SLOT(slot2)) ==========connect(Object3,SIGNAL(signal2),Object2,SLOT(slot2))

###b.clicked.connect(app.quit)