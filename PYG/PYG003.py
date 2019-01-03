import pygame,sys   #引用
import pygame.freetype

pygame.init()       #初始化
size = width,height = 600,400
speed = [1,1]
BLACK = 0,0,0
GOLD = 255,251,0
pos = [320,100]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Ball")
f1 = pygame.freetype.Font("C:\\Windows\\Fonts\\msyh.ttc",36)
#f1rect = f1.render_to(screen,pos,"世界",fgcolor=GOLD,size=50)
f1surf,f1rect = f1.render("世界",fgcolor=GOLD,size=50)
fps = 300
fclock = pygame.time.Clock()

ball = pygame.image.load("F:\\图库and\jihuang\\flashlight.jpg") #\f转义了
ballrect = ball.get_rect()  #初始化

while True:     #事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])
    if pos[0] < 0 or pos[0]+f1rect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1]+f1rect.height > height:
        speed[1] = -speed[1]    #事件处理
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    screen.fill(BLACK)#刷新背景色,要在图像生成前面，不然生成的图像就被覆盖了      #窗口刷新
    #f1rect = f1.render_to(screen,pos,"世界",fgcolor=GOLD,size=50)
    screen.blit(f1surf,pos)
    fclock.tick(fps)

    pygame.display.update()     #窗口刷新