from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from . import views

urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password_change/done/$', password_change_done, name='password_change_done'),
    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
]