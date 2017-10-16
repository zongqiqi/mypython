import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField("date published")#发布时间

	def was_published_recently(self):
		return self.pub_date >=timezone.now()-datetime.timedelta(days=1)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question=models.ForeignKey(Question)#外键连接
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text