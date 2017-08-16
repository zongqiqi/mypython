from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
	"""用户学习的主题"""
	text=models.CharField(max_length=200)
	date_added=models.DateTimeField(auto_now_add=True)
	ower=models.ForeignKey(User)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic=models.ForeignKey(Topic)
	text=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	#嵌入Meta类，用于储存管理模型的额外信息，在这里设置一个特殊属性，
	#让Django在需要时使用Enties表示多个条目
	class Meta:
		verbose_name_plural='entries'

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50]+"..."