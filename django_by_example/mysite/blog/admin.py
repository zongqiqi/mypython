from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','publish','status')#设置在管理对象列表中显示的字段
	list_filter=('status','created','publish','author')#右侧边栏根据list_filter属性中指定的字段返回结果
	search_fields=('title','body')
	prepopulated_fields={'slug':('title',)}
	raw_id_fields=('author',)
	date_hierarchy='publish'
	ordering=['status','publish']


admin.site.register(Post,PostAdmin)