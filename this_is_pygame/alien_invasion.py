#-*- coding:utf-8 -*-
import sys
import pygame

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	screen=pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")

	#设置背景颜色
	bg_color=(230,230,230)

	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

		#每次循环时重绘屏幕
		screen.fill(bg_color)

		#显示屏幕绘制
		pygame.display.flip()

run_game()