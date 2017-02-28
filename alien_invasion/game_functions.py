import sys

import pygame

from alien import Alien 

from bullet import Bullet

from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ai_settings, screen, ship, bullets):
	#响应的键盘事件和鼠标事件
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
	#监听键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	# alien.blitme()
	aliens.draw(screen)
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
	bullets.update()
	#删除消失的子弹
	for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
	check_bullet_alien_collsions(ai_settings, screen, ship, aliens, bullets)

	
def check_bullet_alien_collsions(ai_settings, screen, ship, aliens, bullets):
	#检测是否有子弹击中外星人
	#如果打中子弹和外星人一起消失
	collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

	# 删除所有的子弹并创建新的外星人
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, stats, screen, ship, bullets):
	#响应被外星人撞到的飞船
	#将ship_left减一
	if stats.ships_left > 0:
		stats.ships_left -= 1

		#清空外星人列表的核子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人，并将飞船放到屏幕地段中央
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		# 暂停
		sleep(0.5)
	else:
		stats.game_avtive = False


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	#检查外星人是不是到屏幕的边缘

	check_fleet_edges(ai_settings, aliens)
	#更新外星人裙中所有外星人的位置
	aliens.update()

	#检测外星人和飞船间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, aliens, bullets)

	#检查是否有外星人达到屏幕底端
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
	

def fire_bullet(ai_settings, screen, ship, bullets):
	#创建一颗子弹，并将其添加到编组bullets中
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x/(2*alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	#创建一个外星人并将其房间改行
	alien = Alien(ai_settings, screen)
	alien_width =alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.y = alien.rect.height + 2*alien.rect.height*row_number
	alien.rect.x = alien.x
	aliens.add(alien)
	print('**********', alien.y, alien.x, aliens)

def create_fleet(ai_settings, screen, ship, aliens):
	#创建外星人群
	#创建一个外星人，并计算一行容纳多少个外星人
	#外星人间距为外星人的宽度
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	#创建第一行外星人
	for row_number in range(number_rows):
		print('-=-=-=-=-=-==-=-=-', row_number)
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)
		
def get_number_rows(ai_settings, ship_height, alien_height):
	#计算屏幕可容纳多少外星人
	avaliable_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(avaliable_space_y/(2*alien_height))
	return number_rows;


def check_fleet_edges(ai_settings, aliens):
	#外星人达到边界做的措施
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def  change_fleet_direction(ai_settings, aliens):
	#将外星人向下移动
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	#检查是否有外星人达到屏幕低端
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#像飞船一样进行处理
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break







