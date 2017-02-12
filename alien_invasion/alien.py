import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
#表示外星人的类
	def __init__(self, ai_settings, screen):
		#初始化外新人
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载外星人图像，并设置rect属性
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		#每个外星人最初都在屏幕的左上角附近
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#外星人的准确位置
		self.x = float(self.rect.x)
	def blitme(self):
		#在指定出绘制外星人
		self.screen.blit(self.image, self.rect)
