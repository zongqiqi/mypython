# -*- coding:utf-8 -*-

import pygame

class Ship():

	def __init__(self, screen):
		"""初始化飞船并设置初始位置"""
		self.screen = screen

		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images/ship_48.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		#将没艘飞船放在屏幕底部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		#移动标志
		self.moving_right=False
		self.moving_left=False


	def update(self):
		if self.moving_right:
			self.rect.centerx+=1
		if self.moving_left:
			self.rect.centerx-=1

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)