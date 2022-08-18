import sys

import pygame
from settings import Settings
class AlienInvasion:
	"""page 205"""
	def __init__(self):
		#初始化资源
		pygame.init()
		self.settings=Settings()

		self.screen=pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))

		self.screen=pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Alien Invasion")
		self.bg_color=(230,230,230)
	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
			#每次退出循环绘制屏幕

			pygame.display.flip()

if __name__ == '__main__':
	ai=AlienInvasion()
	ai.run_game()
