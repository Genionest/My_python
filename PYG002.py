import pygame, sys
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame最小框架")
GOLD = 255, 251, 0

f1 = pygame.freetype.Font("C:\\Windows\\Fonts\\msyh.ttc", 36)
# f1rect = f1.render_to(screen,(300,200),"字体",fgcolor=GOLD,size=30)
f1surf, f1rect = f1.render("Shijie", fgcolor=GOLD, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(f1surf,(250,100))
    pygame.display.update()
