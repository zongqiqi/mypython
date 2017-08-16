from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	"""注销用户"""
	logout(request)
	return HttpResponseRedirect(reverse('app:index'))

def register(request):
	"""注册新用户"""
	if request.method!='POST':
		#显示空的注册表单
		form=UserCreationForm()
	else:
		#处理填好的表单
		form=UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user=form.save()
			#让用户自动登录，在重定向到主页
			authenticated_user=authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('app:index'))
	context={'form':form}
	return render(request,'users/register.html',context)