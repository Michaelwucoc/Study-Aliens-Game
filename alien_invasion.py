import sys

import pygame

class AlienInvasion:
	"""page 205"""
	def _init_(self):
		pygame.init()

		self.screen=pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Alien Invasion")
	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()

			pygame.display.flip()

if _name_ == "_main_":
	ai=AlienInvasion()
	ai.run_game

	self.screen=pygame.display.set_mode((1200,800))