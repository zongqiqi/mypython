from django.conf.urls import url
from .feeds import LatestPostsFeed

from . import views

urlpatterns=[
	#post views
	# url(r'^$',views.post_list,name='post_list'), #正常的url模式
	# url(r'^$',views.PostListView.as_view(),name='post_list'),#使用类图的url的模式
	url(r'^$',views.post_list,name='post_list'),
	url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list,name='post_list_by_tag'),

	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
		views.post_detail,name='post_detail'),
	url(r'^(?P<post_id>\d+)/share/$',views.post_share,name='post_share'),
	url(r'^feed/$',LatestPostsFeed(),name='post_feed'),

	url(r'^search/$', views.search, name='search'),

]