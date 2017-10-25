from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count

from blog.models import Post,Comment
from .forms import EmailPostForm,CommentForm
from taggit.models import Tag

##一般视图；总的blog页面
def post_list(request,tag_slug=None):
	object_list=Post.published.all()


	#标签模块
	tag=None
	if tag_slug:
		tag=get_object_or_404(Tag,slug=tag_slug)
		object_list=object_list.filter(tags__in=[tag])
	#视图带有一个可选的tag_slug参数，默认是一个None值，参数会带进URL中
	#视图内部构建查询集，取回所有发布状态的帖子，假如给定一个标签slug，
	#	通过get_objects_or_404()用给定的slug来获取标签对象
	# 过滤所有的帖子只留下包含给定标签的帖子.

	paginator=Paginator(object_list,3)
	page=request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer deliver the first page
		posts=paginator.page(1)
	except EmptyPage:
		#If page is out of range deliver last page of result
		posts=paginator.page(paginator.num_pages)


	context={'page':page,'posts':posts,'tag':tag}
	return render(request,'blog/post/list.html',context)

##使用基于类的通用视图（views）
# class PostListView(ListView):
# 	queryset=Post.published.all()
# 	context_object_name='posts'
# 	paginate_by=3
# 	template_name='blog/post/list.html'
#通用视图操作
#1、使用一个特定的查询集（QuerySet），取代取回所有的对象，代替定义一个Queryset属性
#	指定mdoel=Post然后Django会把构建的Post.objects.all()查询集（QuerySet）给我们
#2、使用环境变量posts给查询结果，如果不指定任意的context_object_name默认的变量
#	将会是object_list
#3、对结果进行分页处理，每页只显示3个对象
#4、使用定制的模板（template）来渲染页面，如果不设置默认模板，默认为'blog/post_list.html'



#在视图（views）中操作ModelForms
#具体的blog页面
def post_detail(request,year,month,day,post):
	post=get_object_or_404(Post,slug=post,
							status='published',
							publish__year=year,
							publish__month=month,
							publish__day=day)
	#List of active comments for this post
	comments=post.comments.filter(active=True)
	new_comment=None
	comment_form=''

	if request.method=="POST":
		#A comment was posted
		comment_form=CommentForm(data=request.POST)
		if comment_form.is_valid():
			#Create Comment object but don't save to dadabase yet
			new_comment=comment_form.save(commit=False)
			#Assgin the current post to the comment
			new_comment.post=post
			#Save the comment to the database
			new_comment.save()
		else:
			comment_form=CommentForm()

		# 根据标签检索类似的帖子
	post_tags_ids=post.tags.values_list('id',flat=True)
	similar_posts=Post.published.filter(tags__in=post_tags_ids)\
										.exclude(id=post.id)
	similar_posts=similar_posts.annotate(same_tags=Count('tags'))\
									.order_by('-same_tags','-publish')[:4]

									

	context={'post':post,'comments':comments,'new_comment':new_comment,
				'comment_form':comment_form,'similar_posts':similar_posts}
	return render(request,'blog/post/detail.html',context)


##操作表单的视图
def post_share(request,post_id):
	#retrieve post by id
	post=get_object_or_404(Post,id=post_id,status='published')
	sent=False
	cd={'to':'some place'}
	if request.method=="POST":
		#Form was submitted
		form=EmailPostForm(request.POST)
		if form.is_valid():
			#form field passed validation
			cd =form.cleaned_data
			#...send email
			post_url=request.build_absolute_uri(post.get_absolute_url())
			subject='{}({}) recommends you reading "{}"'.format(cd['name'],
															cd['email'],
															post.title)
			message='Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title,
															post_url,
															cd['name'],
															cd['comments'])
			send_mail(subject,message,'zongqiqi0522@foxmail.com',[cd['to']])
			sent=True
	else:
		form=EmailPostForm()
	context={'post':post,'form':form,'sent':sent,'cd':cd['to']}
	return render(request,'blog/post/share.html',context)
#解释：
# 定义了post_share视图，参数为request对象和post_id
# 使用get_object_or_404快捷方式通过ID获取对应的帖子，并且确保在published状态
# 使用同一个视图来展示初始表单和处理提交以后的数据，利用request.POST用来区分





def search(request):
	q=request.GET['search']
	error_msg=''

	if not q:
		error_msg='请输入关键词'
		return render(request,'blog/search/error.html',{'error_msg':error_msg})

	post_list=Post.objects.filter(body__icontains=q)
	context={'error_msg':error_msg,'post_list':post_list,'q':q}
	return render(request,'blog/search/results.html',context)