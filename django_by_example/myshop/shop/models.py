from django.db import models
from django.core.urlresolvers import reverse

# 我们商店中的商品目录将会由不同的产品组成，每一个产品会有一个名字，一段可选的描述，一张可选的图片，价格，价格，以及库存

class Category(models.Model):
	name=models.CharField(max_length=200,db_index=True)
	slug=models.SlugField(max_length=200,db_index=True,unique=True)

	class Meta:
		ordering=('name',)
		verbose_name='category'
		verbose_name_plural='categories'
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',args=[self.slug])

class Product(models.Model):
	category=models.ForeignKey(Category,related_name='products')
	#这是一个链接向 Category 的 ForeignKey 。这是个多对一（many-to-one）关系。一个产品可以属于一个分类，一个分类也可包含多个产品。
	name=models.CharField(max_length=200,db_index=True)#产品名称
	slug=models.SlugField(max_length=200,db_index=True)#为这个产品建立URL的slug
	image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)#可选的产品图片
	description=models.TextField(blank=True)#可选的产品描述
	price=models.DecimalField(max_digits=10, decimal_places=2)
	#这个是DecimalField（十进制字段），这个字段使用Python的decimal.Decimal元类来保存一个固定精度的十进制数，
	#max_digits属性可用于设定数字的最大值，decimal_places属性用于设置小数位数
	stock = models.PositiveIntegerField()
	#库存——PositiveIntegerField（正整数字段），保存产品库存
	available = models.BooleanField(default=True)#用于展示的产品是否可以购买，可以在目录中操作使产品废弃或生效
	created = models.DateTimeField(auto_now_add=True)#保存创建时间，被创建时，时间保存
	updated = models.DateTimeField(auto_now=True)#保存最后一次更新的时间

	class Meta:
		ordering=('name',)
		index_together = (('id', 'slug'),)#指定id和slug字段共用索引

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id,self.slug])