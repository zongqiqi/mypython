from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager


#创建model manager
class PublishedManager(models.Manager):
	def get_queryset(self):#返回执行过的查询集方法
		return super(PublishedManager,self).get_queryset().filter(status='published')



## 博客体系
class Post(models.Model):
	STATUS_CHOICES=(
		('draft','Draft'),
		('published','Published'),
		)
	title=models.CharField(max_length=250)#对应帖子的标题，在SQL数据库中会被转换为VAECHAR
	slug=models.SlugField(max_length=250,
		unique_for_date='publish')#将会在URLs中使用，slug就是一个短标签，该标签只包含
	#字母、数字、下划线、连线，我们将通过slug字段给我们的blog帖子构建漂亮的、友好的
	#URLs，给该字段添加属性unique_for_data，这样可以使用日期和帖子的slug莱维所有帖子构建
	#URLs，在相同的日期中Django会阻止多篇帖子拥有相同的slug。
	author=models.ForeignKey(User,related_name='blog_posts')#这是一个多对一的外键连接关系，
	#一篇帖子只能由一名用户编写，一名用户可以编写多篇帖子，related_name属性定义了从
	#User到Post的反向关系名
	body=models.TextField()#帖子的主体
	publish=models.DateTimeField(default=timezone.now)#表明帖子的发布时间，设置默认值
	created=models.DateTimeField(auto_now_add=True)#表明帖子的创建时间，自动添加
	updated=models.DateTimeField(auto_now=True)#表明帖子的更新时间，自动更新并保存时间
	status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	#表明当前帖子的展示状态，使用choice参数，限定字段值只能是给予选择中的一个。

	class Meta:
		ordering=('-publish',)

	def __str__(self):
		return self.title

	tags=TaggableManager()#这个tags管理器（manager）允许你给POST对象添加，
							#获取和移除标签


	objects=models.Manager()#The default manager
	published=PublishedManager()#Our custom manager

	def get_absolute_url(self):
		return reverse('blog:post_detail',args=[self.publish.year,
												self.publish.strftime('%m'),
												self.publish.strftime('%d'),
												self.slug])
		#通过strftime方法保证个位数字的月份和日期带上0来构url


## 评论体系
class Comment(models.Model):
	post=models.ForeignKey(Post,related_name='comments')#外键连接post帖子
	#定义多对一关系，一条评论只在一个帖子下面，一个帖子可以有多个评论
	#related_name属性允许我们给这个属性命名，这样就可以利用这个关系从相关联的
		#对象反向定位到这个对象，定义好以后可以通过使用comment.post从一条评论
		#来取到对应的帖子，以及通过使用post.comments.all()来取得一个帖子的所以评论
		#如果没有定义related_name属性，Django会使用这个模型model的名称加上_set
		#(在这里是comment_set)来命名从相关联的对象反向定位到这个对象的manager
	name=models.CharField(max_length=80)
	email=models.EmailField()
	body=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	class Meta:
		ordering=('created',)

	def __str__(self):
		return "Comment by {} on {} .".format(self.name,self.post)