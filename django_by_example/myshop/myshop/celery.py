import os
from celery import Celery
from django.conf import settings

#set the default Django settings module for the  'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myshop.settings')

app=Celery('myshop')#创建一个Celery实例
app.config_from_object('django.conf:settings')#加载项目中任意的定制化配置
app.autodsicover_tasks(lambda:settings.INSTALLED_APPS)#自动查找列举在INSTALLED_APPS设置中的异步任务