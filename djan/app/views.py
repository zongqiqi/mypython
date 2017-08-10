from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	"""学习笔记的主页"""
	return render(request, 'app/index.html')
	# return HttpResponse('Hello World')