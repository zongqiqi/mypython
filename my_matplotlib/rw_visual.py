import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的点都绘制出来
rw=RandomWalk(num_points=5000)
rw.fill_walk()

point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none')

#突出起点和终点
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()