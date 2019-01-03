import pygame,sys   #引用

pygame.init()       #初始化
size = width,height = 600,400
speed = [1,1]
BLACK = 0,0,0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Ball")
ball = pygame.image.load("F:\\图库and\jihuang\\flashlight.jpg") #\f转义了
ballrect = ball.get_rect()  #初始化

while True:     #事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]    #事件处理

    screen.fill(BLACK)#刷新背景色      #窗口刷新
    screen.blit(ball,ballrect)

    pygame.display.update()     #窗口刷新