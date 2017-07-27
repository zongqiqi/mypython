# -*- coding: utf-8  -*-
import sys
from PyQt4 import QtGui#进行一些必要的import操作，基本的GUI组件在QtGui模块中
"""
面向过程编程
"""
app = QtGui.QApplication(sys.argv)#每个PyQt4C程序必须创建一个application对象，application在QtGui模块中，sys.argv参数是命令行中的一组参数
                                  #Python脚本可以在shell中运行，这样，我们可以控制脚本的启动
widget = QtGui.QWidget()#QWidget 窗口组件是PyQt4中所有用户界面对象的基类，我们使用 QWidget 默认的构造，没有父亲。没有父亲的窗口组件称为窗体。（实例化一个QWidget）
widget.resize(250,150)#方法调整了 widget 的大小，宽250像素，高150像素。
widget.setWindowTitle('simple')#这里我们为窗口设置了标题，标题显示在标题栏上。
widget.show()#show() 方法将窗口呈现在屏幕上。

sys.exit(app.exec_())#最后，我们输入应用程序的主事件循环，事件处理从这里开始。主事件循环从窗口系统接收事件并分发到应用程序的窗口组件上。
                     # 当主事件循环结束，如果我们调用 exit() 方法或者主窗口组件被销毁。 sys.exit() 方法确保干净的退出。将通知环境应用程序是如何结束的。