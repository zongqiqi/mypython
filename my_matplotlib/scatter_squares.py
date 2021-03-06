import matplotlib.pyplot as plt

#绘制单点======================================
# plt.scatter(2,4)
# plt.scatter(2,4,s=200)#实参s设置了绘制图形时使用的点的尺寸

#绘制散点图================================================
# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]

# plt.scatter(x_values,y_values,s=100)

# #设置图表的标题，并给坐标轴添加标签
# plt.title("Square Number",fontsize=24)
# plt.xlabel("Value",fontsize=24)
# plt.ylabel("Square of Value",fontsize=14)

# #设置刻度标记的大小
# plt.tick_params(axis='both',which='major',labelsize=14)

# plt.show()

# x_values=list(range(1,1000))
# y_values=[x**2 for x in x_values]

# plt.scatter(x_values,y_values,c='red',edgecolor='none',s=1)
# #edgecolor='none'设置取消数据点的轮廓
# #c='red'设置数据点的颜色

# plt.title("Square Number",fontsize=24)
# plt.xlabel("Value",fontsize=24)
# plt.ylabel("Square of Value",fontsize=14)

# #设置每个坐标轴的取值范围
# plt.axis([0,1100,0,1100000])

# plt.show()

#颜色渐变效果====================================
x_values=list(range(1001))
y_values=[x**2 for x in x_values]
#把参数c设置为y值列表，并使用cmap告诉pyplot使用哪个颜色进行映射
#     y值较小的颜色较浅，y值大的颜色深
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

# plt.show()

#自动保存图表，第一个参数指定以什么样的文件名保存图表，第二个参数指定将
#    多余的空白部分裁掉
plt.savefig('squares_plot.png',bbox_inches='tight')