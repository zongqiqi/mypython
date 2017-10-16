from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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