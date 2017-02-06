import sys

import pygame

def check_events():
	#监听键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def update_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()