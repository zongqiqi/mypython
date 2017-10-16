#4.0
# from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse,HttpResponseRedirect
# from django.core.urlresolvers import reverse
# # from django.template import RequestContext,loader

# from .models import Question,Choice

# def index(request):
# 	# return HttpResponse("Hello,world.You're at the polls index")#1.0
# 	latest_question_list=Question.objects.order_by('pub_date')
# 	# output=', '.join([p.question_text for p in latest_question_list])#2.0
# 	# return HttpResponse(output)#2.0
# 	# template=loader.get_template('polls/index.html')#3.0
# 	# context={
# 	# 		'latest_question_list':latest_question_list,#3.0
# 	# 	}
# 	# return HttpResponse(template.render(context))#3.0
# 	context={"latest_question_list":latest_question_list}
# 	return render(request,'polls/index.html',context)

# def detail(request,question_id):
# 	# return HttpResponse("You're looking at question %s."%question_id)#1.0
# 	# try:
# 	# 	question=Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exist.")
# 	# return render(request,"polls.detail.html",{"question":question})#2.0
# 	question=get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/detail.html',{'question':question})

# def results(request,question_id):
# 	# response="You're looking at results of question %s ."
# 	# return HttpResponse(response % question_id)#1.0
# 	question=get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/results.html',{"question":question})

# def vote(request,question_id):
# 	# return HttpResponse("You're voying question %s"%question_id)#1.0
# 	p=get_object_or_404(Question,pk=question_id)
# 	try:
# 		selected_choice=p.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError,Choice.DoesNotExist):
# 		return render(request,'polls/detail.html',{"question":p,'error_message':"You don't select a choice."})
# 	else:
# 		selected_choice.votes+=1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))




from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice,Question

class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
# def index(request):
# 	latest_question_list=Question.objects.order_by('pub_date')
# 	context={"latest_question_list":latest_question_list}
# 	return render(request,'polls/index.html',context)

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
# def detail(request,question_id):
# 	question=get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/detail.html',{'question':question})

class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'
# def results(request,question_id):
# 	question=get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/results.html',{"question":question})

def vote(request,pk):
	# return HttpResponse("You're voying question %s"%question_id)#1.0
	p=get_object_or_404(Question,pk=pk)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{"question":p,'error_message':"You don't select a choice."})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

