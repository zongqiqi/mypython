from django.contrib import admin
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
	list_display=['name','slug']
	prepopulated_fields={'slug':('name',)}#指定那些要使用其他字段来自动赋值的字段
admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
	list_display=['name','slug','price','stock','available','created','updated']
	list_filter=['available','created','updated']
	list_editable=['price','stock','available']
	prepopulated_fields={'slug':('name',)}
admin.site.register(Product,ProductAdmin)