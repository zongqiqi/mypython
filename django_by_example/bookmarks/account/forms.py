from django import forms
from django.contrib.auth.models import User

from .models import Profile


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # 使用PasswordInput控件来渲染HTML input元素

#用户注册模块
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
        	raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """
    允许用户编辑他们的first name ，last name，email，
    这些储存在User模型中的内置字段
    """
    class Meta:
        model=User
        fieds=('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    """
    允许用户编辑我们储存在定制的Profile模型中的额外数据，
    """
    class Meta:
        model=Profile
        fields=('date_of_birth','photo')