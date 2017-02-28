import game_functions as gf

import pygame

from settings import Settings

from ship import Ship

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button

def  run_game():
	#初始化创建屏幕对象
	pygame.init()

	ai_settings = Settings()

	#创建用于存储游戏信息的实例
	stats = GameStats(ai_settings)
	
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Incasion")

	bg_color = ai_settings.bg_color
	screen.fill(bg_color)

	#创建飞船
	ship = Ship(ai_settings, screen)

	#创建存储子弹的编组
	bullets = Group()
	aliens = Group()

	#创建外星人
	# alien = Alien(ai_settings, screen)
	gf.create_fleet(ai_settings, screen, ship, aliens)

	play_button = Button(ai_settings, screen, "Play")

	#开始游戏的主循环
	while True:

		# ship.blitme()

		#监听键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)

		if stats.game_active:

			ship.update()

			# bullets.update()

			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

		#让最近绘制的屏幕可见
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
		# pygame.display.flip()

run_game()
