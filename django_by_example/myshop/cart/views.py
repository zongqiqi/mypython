from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from cart.forms import CartAddProductForm

@require_POST#只接受POST请求
def cart_add(request,product_id):#接收产品id作为参数--------添加购物车
	cart=Cart(request)
	product=get_object_or_404(Product,id=product_id)#检索要添加的产品
	form=CartAddProductForm(request.POST)
	if form.is_valid():#表单验证
		cd =form.cleaned_data#清理表单
		cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
	return redirect('cart:cart_detail')#重定向到cart主页

def cart_remove(request,product_id):#删除购物车
	cart=Cart(request)
	product=get_object_or_404(Product,id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')

def cart_detail(request):#购物车主页视图
	cart=Cart(request)
	for item in cart:
		item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})

	context={'cart':cart}
	return render(request,'cart/detail.html',context)

#stupid
# def product_detail(request,id,slug):
# 	product=get_object_or_404(Product,id=id,slug=slug,available=True)
# 	cart_product_form=CartAddProductForm()

# 	context={'product':product,'cart_product_form':cart_product_form}
# 	return render(request,'shop/product/detail.html',context)