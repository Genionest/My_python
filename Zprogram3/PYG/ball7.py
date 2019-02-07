import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("#",event.key,event.mod)
            else:
                print(event.unicode,event.key,event.mod)
        if event.type == pygame.MOUSEMOTION:
            print("[MouseMotion]",event.pos,event.rel,event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MouseButtonUp]",event.pos,event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MouseButtonDown]",event.pos,event.button)
    pygame.display.update()