from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

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

def new_topic(request):
	"""添加新主题"""
	if request.method !='POST':
		"""未提交数据，创建一个新表单"""
		form=TopicForm()
		context={'form':form}
		return render(request,'app/new_topic.html',context)
	else:
		#POST提交的数据，对数据进行处理
		form=TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('app:topics'))

def new_entry(request,topic_id):
	"""在特定的主题中添加条目"""
	topic=Topic.objects.get(id=topic_id)

	if request.method!='POST':
		form=EntryForm()
	else:
		#post提交数据，对数据进行处理
		form=EntryForm(data=request.POST)
		if form.is_valid():
			new_entry=form.save(commit=False)
			new_entry.topic=topic
			new_entry.save()
			return HttpResponse(reverse('app:topic',args=[topic_id]))
	context={'topic':topic,'form':form}
	return render(request,'app/new_entry.html',context)

def edit_entry(request,entry_id):
	"""编辑既有的条目"""
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic

	if request.method!='POST':
		#初次请求，使用当前条目填充表单
		form=EntryForm(instance=entry)
	else:
		#POST提交的数据，对entry数据进行处理
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse(reverse('app:topic',args=[topic.id]))
	context={'entry':entry,'topic':topic,'form':form}
	return render(request,'app/edit_entry.html',context)

