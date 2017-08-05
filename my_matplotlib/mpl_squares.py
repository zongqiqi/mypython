#中文测试，Python3不需要在coding：utf-8
import matplotlib.pyplot as plt#导入模块

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]#数据
# plt.plot(squares)#绘制图像
# plt.plot(squares,linewidth=5)#设置绘制线条的粗细
plt.plot(input_values,squares,linewidth=5)

#设置图表标题，并给坐标轴添加标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)#xlabel和ylabel设置坐标轴标题
plt.ylabel("Square of value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.show()#创建屏幕显示图像