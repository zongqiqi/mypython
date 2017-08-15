"""定义app的URL映射关系"""

from django.conf.urls import url

#句点号让Python从当前的urls.py模块所在的文件夹导入视图模块
from . import views

#URL模式是对函数url()的调用，三个参数：第一个是正则表达式；第二个是
#				要调用的视图函数，第三个是将URL模式命名
urlpatterns=[
	#主页
	url(r'^$',views.index,name='index'),

	#显示所有的主题
	url(r'^topic/$',views.topics,name='topics'),

	#显示特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

	#用于添加新主题的网页
	url(r'^new_topic/$',views.new_topic,name='new_topic'),

	#用于添加新条目的页面
	url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),

	#用于编辑条目的页面
	url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),

	#
]