# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui
"""
面向对象编程：在面向对象编程中三个最重要东西是类、数据和方法
"""
class Icon(QtGui.QWidget):#创建一个新的类，继承自QtGui.QWidget
    def __init__(self,parent=None):#Icon类初始化
        QtGui.QWidget.__init__(self,parent)#Icon类的父类QtGui.QWidget初始化

        self.setGeometry(300,300,250,150)#定义窗体在屏幕上的位置，并设定大小，（x,y,w,h)
        self.setWindowTitle('icon')#设置窗体名称
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))#设置窗体图片（当前文件夹下的icons文件夹里面的web.png图片）

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())