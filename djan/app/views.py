from django.shortcuts import render
from django.http import HttpResponse

from .models import Topic

# Create your views here.
def index(request):
	"""学习笔记的主页"""
	return render(request, 'app/index.html')
	# return HttpResponse('Hello World')

def topics(request):
	"""显示所有的主题"""
	topics=Topic.objects.order_by('date_added')
	context={'topics':topics}
	return render(request,'app/topics.html',context)

def topic(request,topic_id):
	"""显示单个主题及其所有条目"""
	topic=Topic.objects.get(id=topic_id)
	entries=topic.entry_set.order_by('-date_added')
	context={'topic':topic,'entries':entries}
	return render(request,'app/topic.html',context)