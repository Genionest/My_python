from tkinter import *

window = Tk()
window.title("调色器")
window.geometry("400x400")

color = '#000000'

def rgbstr(n): #将int转化为两个字符
    rn = str(hex(n)).lstrip('0x')
    if len(rn)<2:
        rn = '0'+rn
    if n ==0:
        rn = '00'
    return(rn)
#利用切片方法对color字符对应位置的两个字符进行替换，
#但不能直接替换，因为str是不可变对象，只能通过赋值
def scroll_scale1(v):
    global color
    r = rgbstr(int(v))
    color = color[0]+r+color[3:]
    canvas.config(bg=color)
    var.set(color)

def scroll_scale2(v):
    global color
    g = rgbstr(int(v))
    color = color[0:3]+g+color[5:]
    canvas.config(bg=color)
    var.set(color)

def scroll_scale3(v):
    global color
    b = rgbstr(int(v))
    color = color[:5]+b
    canvas.config(bg=color)
    var.set(color)

canvas = Canvas(window,bg='#000000',height=100,width=200)

sr = Scale(window,label='红色',from_=0,to=255,orient=HORIZONTAL,
           length=256,showvalue=1,tickinterval=256/3,resolution=1,
           command=scroll_scale1)
sg = Scale(window,label='绿色',from_=0,to=255,orient=HORIZONTAL,
           length=256,showvalue=1,tickinterval=256/3,resolution=1,
           command=scroll_scale2)
sb = Scale(window,label='蓝色',from_=0,to=255,orient=HORIZONTAL,
           length=256,showvalue=1,tickinterval=256/3,resolution=1,
           command=scroll_scale3)

var = StringVar()
L1 = Label(window,textvariable=var,font=('Arial',10),width=10,height=1)

canvas.pack()
sr.pack()
sg.pack()
sb.pack()
L1.pack()

window.mainloop()
