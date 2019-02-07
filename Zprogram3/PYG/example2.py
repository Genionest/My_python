import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame事件处理")
fps = 1
fclok = pygame.time.Clock()
num = 1

while True:
    uevent = pygame.event.Event(pygame.KEYDOWN,{"unicode":123,"key":pygame.K_SPACE,"mod":pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("#",event.key,event.mod)
            else:
                print(event.unicode,event.key,event.mod)

    pygame.display.update()