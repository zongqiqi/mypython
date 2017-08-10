from django.shortcuts import render

# Create your views here.
def index(request):
	"""学习笔记的主页"""
	return render(request,'app/index.html')