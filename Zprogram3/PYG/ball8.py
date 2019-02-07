import pygame,sys

pygame.init()
icon = pygame.image.load("F:\图库and\\app_pic\cute_QRcode.png")
pygame.display.set_icon(icon) #设置图标
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
still = False
bgcolor = pygame.Color("black")

def RGBchannel(a):
    return 0 if a<0 else(255 if a>255 else int(a))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果是退出事件
            sys.exit()
        elif event.type == pygame.KEYDOWN: #如果是键盘按下事件
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
        elif event.type == pygame.VIDEORESIZE: #更新窗体大小
            size = width,height = event.size[0],event.size[1]
            pygame.display.set_mode(size,pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:#按下左键，小球停止移动
            if event.button == 1: #作用在左键
                still = True
        elif event.type == pygame.MOUSEBUTTONUP: #释放左键，小球位移到鼠标处，并继续移动
            still = False
            if event.button == 1: #作用在左键
                ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)
        elif event.type == pygame.MOUSEMOTION: #鼠标移动并且左键一直按下，即左键拖动鼠标
            if event.buttons[0] == 1:  #作用在左键
                #小球位移到使ballrect的左上定点在鼠标pos处
                ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)

    if pygame.display.get_active() and not still: #窗口没有最小化才继续移动,条件+still为False
        ballrect = ballrect.move(speed)#ballrect不指代小球，而是指代小球应该出现的区域
        #move方法使这个区域移动，也就是说ballrect实际的属性至少有面积、位置
    if ballrect.left <0 or ballrect.right > width:
        speed[0] = - speed[0]
        #小球超出范围的方向处理，因为小球只会在鼠标pos的右下方出现
        #所以鼠标pos在screen内，小球不会超出左边和上边的边界
        #也就只考虑右边和下边的情况
        if ballrect.right > width and ballrect.right+speed[0] > width:
            speed[0] = - abs(speed[0]) #超出范围，速度只能向左
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > height:
            speed[1] = - abs(speed[1]) #超出范围，速度只能向上

    bgcolor.r = RGBchannel(ballrect.left*255/width)
    bgcolor.g = RGBchannel(ballrect.top*255/height)
    bgcolor.b = RGBchannel(min(speed[0],speed[1])/max(speed[0],speed[1],1)*255)

    fclock.tick(fps)
    screen.fill(bgcolor)
    screen.blit(ball,ballrect)

    pygame.display.update()