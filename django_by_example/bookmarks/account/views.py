from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

from .forms import LoginForm,UserRegistrationForm,UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			user=authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponse('Authneticated successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')

	else:
		form=LoginForm()

	context={'form':form}
	return render(request,'account/login.html',context)


@login_required
def dashboard(request):
	return render(request,'account/dashboard.html',{'section':'dashboard'})


def register(request):
	if request.method == 'POST':
		user_form=UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user objects but avoid saving it yet.
			new_user=user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile=Profile.objects.create(user=new_user)
			return render(request,'account/register_done.html',
				{'new_user':new_user})
	else:
		user_form=UserRegistrationForm()
	return render(request,'account/register.html',{'user_form':user_form})


def password_change_done1(request):
	return render(request,'account/regrstration/password_change_done.html',)



@login_required
def edit(request):
	if request.method=="POST":
		user_form=UserEditForm(instance=request.user.profile,
				data=request.POST)
		profile_form=ProfileEditForm(instance=request.user.profile,
				data=request.POST,files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form=UserEditForm(instance=request.user)
		profile_form=ProfileEditForm(instance=request.user.profile)
	return render(request,'account/edit.html',
			{'user_form':user_form,'profile_form':profile_form})