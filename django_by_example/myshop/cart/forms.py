from django import forms

PRODUCT_QUANTITY_CHOICE=[(i,str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
	"""
	用户选择产品数量的表单
	"""
	quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE,coerce=int)#数量限制1-20，使用TyepedChoiceField和coerce把
																				#输入的数字转换为整数
	update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
					#展示数量是否要加进当前的产品数量上(false)