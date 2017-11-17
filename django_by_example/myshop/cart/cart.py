from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
	def __init__(self,request):
		"""
		Initialize the cart.
		"""
		self.session=request.session
		cart=self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save the empty cart in session
			cart=self.session[settings.CART_SESSION_ID]={}
		self.cart=cart
#这个cart类用于管理购物车，把一个购物车一同初始化，使用self.session=request.session保存当前对话以便其对cart的其他方法使用，
#首先尝试self.session.get(settings.CART_SESSION_ID)尝试从当前会话中获取购物车，如果当前会话中没有购物车就在会话中设置一个空字典，
#空购物车，购物车字典使用ID作为键，以数量和价格键值对作为字典的值，通过这样保证一个产品在购物车中不会被重复添加
	def add(self,product,quantity=1,update_quantity=False):#
		"""
		Add a product to the cart or update its quantity
		"""
		product_id = str(product.id)# Django 使用 JSON 来序列化会话数据，而 JSON 又只接受字符串的键名
		if product_id not in self.cart:
			self.cart[product_id]={'quantity':0,'price':str(product.price)}
		if update_quantity:
			self.cart[product_id]['quantity']=quantity
		else:
			self.cart[product_id]['quantity']+=quantity
		self.save
#add() 函数接受以下参数
#product：需要在购物车中更新或者向购物车添加的 Product 对象
#quantity：一个产品数量的可选参数。默认为 1
#update_quantity：这是一个布尔值，它表示数量是否需要按照给定的数量参数更新（True），不然新的数量必须要被加进已存在的数量中（False）
	def save(self):
		#update the session cart
		self.session[settings.CART_SESSION_ID]=self.cart#把购物车数据同步到会话
		#mark the session as 'modified' to make sure it is saved
		self.session.modified=True
		# session.modified = True 标记改动了的会话。这是为了告诉 Django 会话已经被改动，需要将它保存起来。
	def remove(self,product):
		"""
		remove a product from the cart
		"""
		product_id=str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()
	def __iter__(self):
		"""
		Iterate over the items in the cart and get the product from the database
		"""
		product_ids=self.cart.keys()#获取购物车中的商品ID
		#get the product objects and add them  to the cart
		products=Product.objects.filter(id__in=product_ids)#由商品ID获取product对象
		for product in products:
			self.cart[str(product.id)]['product']=product
		for item in self.cart.values():
			item['price']=Decimal(item['price'])
			item['total_price']=item['quantity']*item['price']
			yield item
	def __len__(self):
		"""
		Count all items in cart
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		"""
		remove cart from the session
		"""
		del self.session[settings.CART_SESSION_ID]
		self.session.modified=True