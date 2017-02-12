import pygame

class Ship():
	def __init__(self, ai_seetings, screen):
		self.screen = screen
		self.ai_seetings = ai_seetings

		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom;

		#获取飞船属性center中存储最小数值
		self.center = float(self.rect.centerx)

		#移动标示
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_seetings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_seetings.ship_speed_factor

		self.rect.centerx = self.center
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
