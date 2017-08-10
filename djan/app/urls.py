"""定义app的URL映射关系"""

from django.conf.urls import url

#句点号让Python从当前的urls.py模块所在的文件夹导入视图模块
from . import views

#URL模式是对函数url()的调用，三个参数：第一个是正则表达式；第二个是
#				要调用的视图函数，第三个是将UURL模式命名
urlpatterns=[
	#主页
	url(r'^$',views.index,name='index'),
]