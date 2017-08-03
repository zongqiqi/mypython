#-*- coding:utf-8 -*-

class Settings(object):
	"""docstring for Settings"""
	def __init__(self):
		self.screen_width=800#屏幕宽
		self.screen_height=600#屏幕高度
		self.bg_color=(230,230,230)#屏幕颜色

		#飞船的设置
		self.ship_speed_factor=1.5

		#子弹设置
		self.bullet_speed_factor=1#子弹移动速度
		self.bullet_width=10#子弹宽3像素
		self.bullet_height=15#子弹高15像素
		self.bullet_color=60,60,60
		self.bullets_allowed=10000

		#外星人设置
		self.alien_speed_factor=0.5
		self.fleet_drop_speed=10
		self.fleet_direction=1#向右移动
