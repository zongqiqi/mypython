#-*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self, ai_settings,screen):
		"""初始化外星人并设置起始位置"""
		super(Alien, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		#加载外星人图片，并设置rect属性
		self.image=pygame.image.load("images/alien_32.png")
		self.rect=self.image.get_rect()

		#设置外星人的初始位置
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		#储存外星人的准确位置
		self.x=float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image,self.rect)
		