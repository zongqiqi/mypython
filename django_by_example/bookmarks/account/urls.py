from django.conf.urls import url
from django.contrib.auth import  views as auth_views


from . import views


urlpatterns=[
	# url(r'^login/$',views.user_login,name='login'),
	url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'},name='login'),
	url(r'^logout/$', auth_views.logout,{'template_name': 'registration/logged_out.html'}, name='logout'),
	# url(r'^logout/$', views.logoutt, name='logout'),
	url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
	# change password
	url(r'^password-change/$', auth_views.password_change, name='password_change'),
	url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
	# reset password
	## restore password urls
	url(r'^password-reset/$',auth_views.password_reset,name='password_reset'),
	url(r'^password-reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
				auth_views.password_reset_confirm,name='password_reset_confirm'),
	url(r'^password-reset/complete/$',auth_views.password_reset_complete,
						name='password_reset_complete'),

	url(r'^$',views.dashboard,name='dashboard'),
]
