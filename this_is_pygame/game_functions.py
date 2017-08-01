#-*- coding:utf-8 -*-

import sys
import pygame
from bullet import Bullte

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key ==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		#创建一个子弹，加入编组
		if len(bullets)<ai_settings.bullets_allowed:
			new_bullet=Bullte(ai_settings,screen,ship)
			bullets.add(new_bullet)

def check_keyup_events(event,ship):
	"""按键响应松开"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	if event.key==pygame.K_LEFT:
		ship.moving_left=False


def check_events(ai_settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		#响应按键
		elif event.type==pygame.KEYDOWN:
			# if event.key==pygame.K_RIGHT:
			# 	ship.moving_right=True
			# elif event.key==pygame.K_LEFT:
			# 	ship.moving_left=True
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type==pygame.KEYUP:
			# if event.key==pygame.K_RIGHT:
			# 	ship.moving_right=False
			# elif event.key==pygame.K_LEFT:
			# 	ship.moving_left=False
			check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets):
	"""更新屏幕上的图像，并切换到新的屏幕"""
	#每次循环都重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	#让最近的绘制屏幕可见
	pygame.display.flip()