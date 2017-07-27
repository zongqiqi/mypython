# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
"""
Qt提供了很多关于获取窗体位置及显示区域大小的函数，本实例利用一个简单的对话框显
示窗体的各种位置信息，包括窗体的所在点位置，长，宽信息等。本实例的目的是分析各个
有关位置信息的函数之间的区别，如 x(),y(),pos(),rect(),size(),geometry()等，以及在不同的
情况下应使用哪个函数来获取位置信息

x(),y(),frameGeometry(),pos(),geometry(),width(),height(),rect(),size()几个函数，这几个函
数均是 QWidget提供的。当改变对话框的大小，或移动对话框时，调用各个函数所获得的
信息显示也相应地发生变化
"""
class Geometry(QDialog):
    def __init__(self, parent=None):
        super(Geometry, self).__init__(parent)
        self.setWindowTitle("Geometry")
        Label1 = QLabel("x0:")
        Label2 = QLabel("y0:")
        Label3 = QLabel("frameGeometry():")
        Label4 = QLabel("pos():")
        Label5 = QLabel("geometry():")
        Label6 = QLabel("width():")
        Label7 = QLabel("height():")
        Label8 = QLabel("rect():")
        Label9 = QLabel("size():")

        self.xLabel = QLabel()
        self.yLabel = QLabel()
        self.frameGeoLabel = QLabel()
        self.posLabel = QLabel()
        self.geoLabel = QLabel()
        self.widthLabel = QLabel()
        self.heightLabel = QLabel()
        self.rectLabel = QLabel()
        self.sizeLabel = QLabel()

        layout = QGridLayout()
        layout.addWidget(Label1, 0, 0)

        layout.addWidget(self.xLabel, 0, 1)
        layout.addWidget(Label2, 1, 0)
        layout.addWidget(self.yLabel, 1, 1)
        layout.addWidget(Label3, 2, 0)
        layout.addWidget(self.frameGeoLabel, 2, 1)
        layout.addWidget(Label4, 3, 0)
        layout.addWidget(self.posLabel, 3, 1)
        layout.addWidget(Label5, 4, 0)
        layout.addWidget(self.geoLabel, 4, 1)
        layout.addWidget(Label6, 5, 0)
        layout.addWidget(self.widthLabel, 5, 1)
        layout.addWidget(Label7, 6, 0)
        layout.addWidget(self.heightLabel, 6, 1)
        layout.addWidget(Label8, 7, 0)
        layout.addWidget(self.rectLabel, 7, 1)
        layout.addWidget(Label9, 8, 0)
        layout.addWidget(self.sizeLabel, 8, 1)

        self.setLayout(layout)
        self.updateLabel()###程序初始化时调用 updateLabel()函数，以获得各位置函数的信息并显示。updateLabel()函数负责调用各个位置函数获得结果并显示。

    def moveEvent(self, event):###重定义 QWidget的  moveEvent()和 resizeEvent()函数，分别响应对话框的移动事件和调整
        self.updateLabel()      ###大小事件，使得窗体在被移动或窗体大小发生改变时，能同步更新各函数结果的显示。

    def resizeEvent(self, event):
        self.updateLabel()

    def updateLabel(self):
        temp = QString()

        self.xLabel.setText(temp.setNum(self.x()))###x(),y()和 pos()函数都是获得整个窗体左上角的坐标位置
        self.yLabel.setText(temp.setNum(self.y()))
        self.frameGeoLabel.setText(temp.setNum(self.frameGeometry().x()) + ","+###frameGeometry()与  geometry()相对应，frameGeometry()是获得整个窗体的左上顶点和长，宽值，
                                   temp.setNum(self.frameGeometry().y()) + "," +###而 geometry()函数获得的是窗体内中央区域的左上顶点坐标以及长，宽值。
                                   temp.setNum(self.frameGeometry().width()) + "," +
                                   temp.setNum(self.frameGeometry().height()))
        self.posLabel.setText(temp.setNum(self.pos().x()) + "," +
                        temp.setNum(self.pos().y()))###x(),y()和 pos()函数都是获得整个窗体左上角的坐标位置
        self.geoLabel.setText(temp.setNum(self.geometry().x()) + "," +
                        temp.setNum(self.geometry().y()) + "," +###geometry()函数获得的是窗体内中央区域的左上顶点坐标以及长，宽值。
                        temp.setNum(self.geometry().width()) + "," +
                        temp.setNum(self.geometry().height()))
        self.widthLabel.setText(temp.setNum(self.width()))
        self.heightLabel.setText(temp.setNum(self.height()))
        self.rectLabel.setText(temp.setNum(self.rect().x()) + "," +
                    temp.setNum(self.rect().y()) + "," +
                    temp.setNum(self.rect().width()) + "," +###直接调用 width()和 height()函数获得的是中央区域的长和宽的值。
                    temp.setNum(self.rect().height()))
        self.sizeLabel.setText(temp.setNum(self.size().width()) + "," +###rect()和 size()，调用它们获得的结果也都是对于窗体的中央区域而言的，
                    temp.setNum(self.size().height()))###size()获得的是窗体中央区域的长，宽值，rect()与 geometry()一样返回一个 QRect对象。

app=QApplication(sys.argv)
form=Geometry()
form.show()
app.exec_()


"""
在实际应用中需根据情况使用正确的位置信息函数以获得准确的位置尺寸信息，尤其
是在编写对位置精度要求较高的程序时，如地图浏览程序，更应注意函数的选择，避免产生
不必要的误差。

在编写程序时，初始化窗体时最好不要使用 setGeometry()函数，而用 resize()和 move()函
数代替，因为使用 setGeometry()会导致窗体 show()之后在错误的位置上停留很短暂的一段
时间，带来闪烁现象。
"""




