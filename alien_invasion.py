import sys

import pygame

class AlienInvasion:
	"""page 205"""
	def __init__(self):
		#初始化资源
		pygame.init()

		self.screen=pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Alien Invasion")
		self.bg_color=(230,230,230)
	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
			#每次退出循环绘制屏幕
					self.screen.fill(self.bg_color)
			#让绘制屏幕可见
			pygame.display.flip()

if __name__ == '__main__':
	ai=AlienInvasion()
	ai.run_game()
