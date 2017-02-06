import game_functions as gf

import pygame

from settings import Settings

from ship import Ship

def  run_game():
	#初始化创建屏幕对象
	pygame.init()

	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Incasion")

	bg_color = ai_settings.bg_color
	screen.fill(bg_color)

	ship = Ship(screen)

	#开始游戏的主循环
	while True:

		ship.blitme()

		#监听键盘和鼠标事件
		gf.check_events()

		#让最近绘制的屏幕可见
		gf.update_screen(ai_settings, screen, ship)
		# pygame.display.flip()

run_game()
