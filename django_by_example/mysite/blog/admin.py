from django.contrib import admin
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','publish','status')#设置在管理对象列表中显示的字段
	list_filter=('status','created','publish','author')#右侧边栏根据list_filter属性中指定的字段返回结果
	search_fields=('title','body')#定义一个搜索字段列
	prepopulated_fields={'slug':('title',)}#通过输入的标题自动填充slug字段
	raw_id_fields=('author',)#
	date_hierarchy='publish'#在搜索框下面显示一个通过时间层快速导航的栏
	ordering=['status','publish']#默认排序方式


##注册评论
class CommentAdmin(admin.ModelAdmin):
	list_display=('name','email','post','created','active')
	list_filter=('active','created','updated')
	search_fields=('name','email','body')




admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)