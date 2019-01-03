import pygame,sys

pygame.init()
#vInfo = pygame.display.Info()
#size = width,height = vInfo.current_w,vInfo.current_h
size = widht,height = 600,400
BLACK = 0,0,0
speed = [1,1]

screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Move Ball")
ball = pygame.image.load("F:\\图库and\jihuang\\flashlight.jpg")
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果是退出事件
            sys.exit()
        if event.type == pygame.KEYDOWN: #如果是键盘按下事件
            if event.key == pygame.K_LEFT: #如果速度的绝对值大于0，则继续-1；等于0就不减
                speed[0] = speed[0] if speed[0]==0 else (abs(speed[0])-1)*int(speed[0]/(abs(speed[0])))
            elif event.key == pygame.K_RIGHT: #如果速度大于0，就+1；速度小于0，就-1
                speed[0] = speed[0]+1 if speed[0]>0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1]+1 if speed[1]>0 else speed[1]-1
            elif event.key == pygame.K_DOWN: #如果速度的绝对值大于0，则继续-1；等于0就不减
                speed[1] = speed[1] if speed[1]==0 else (abs(speed[1])-1)*int(speed[1]/(abs(speed[1])))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.VIDEORESIZE: #更新窗体大小
            size = width,height = event.size[0],event.size[1]
            pygame.display.set_mode(size,pygame.RESIZABLE)

    ballrect = ballrect.move(speed)
    if ballrect.left <0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    fclock.tick(fps)
    screen.fill(BLACK)
    screen.blit(ball,ballrect)

    pygame.display.update()