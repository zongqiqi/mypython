from django import forms


#登录表单
class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)
		#使用PasswordInput控件来渲染HTML input元素