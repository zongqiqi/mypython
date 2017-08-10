from django.contrib import admin

# Register your models here.

from app.models import Topic,Entry

#使用register让Django通过管理网站管理模型
admin.site.register(Topic)
admin.site.register(Entry)