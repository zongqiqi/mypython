from django.db import models
from django.conf import settings


#拓展User模型

class Profile(models.Model):
	"""
	拓展User模型，包含额外的数据，创建一个“Profile”模型，包含所有的额外的字段
	并且和Django的User模型做一对一的关联
	"""
	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth=models.DateField(blank=True,null=True)
	photo=models.ImageField(upload_to='users/%Y/%M/%d',blank=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)