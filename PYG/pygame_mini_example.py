# Unit MiniExample:Pygame Hello World Game
import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame最小框架")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.update()