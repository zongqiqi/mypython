#-*- coding:utf-8 -*-

import sys
import pygame


def check_events(ship):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		#响应按键
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=True
			elif event.key==pygame.K_LEFT:
				ship.moving_left=True

		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=False
			elif event.key==pygame.K_LEFT:
				ship.moving_left=False



def update_screen(ai_settings,screen,ship):
	"""更新屏幕上的图像，并切换到新的屏幕"""
	#每次循环都重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	#让最近的绘制屏幕可见
	pygame.display.flip()