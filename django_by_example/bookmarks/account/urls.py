from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login

from . import views

urlpatterns=[

	#post views
	# url(r'^login/$',views.user_login,name='login'),
	#登录
	url(r'^login/$',login,name='login'),
	#登出
	url(r'^logout/$',logout,name='logout'),
	#重新登录
	url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),

	url(r'^$',views.dashboard,name='dashboard'),

]