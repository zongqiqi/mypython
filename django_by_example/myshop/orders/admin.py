from django.contrib import admin
from .models import Order,OrderItem



class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email','address', 'postal_code', 'city', 'paid','created', 'updated']
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]#使用OrderItemline来把OrderItem引用为OrderAdmin类的内联类
							   #内联类允许你在同一个编辑页面引用模型，并且将这个模型作为父模型
admin.site.register(Order, OrderAdmin)