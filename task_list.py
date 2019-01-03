from tkinter import Tk,Button,Listbox,StringVar,Label
from random import shuffle

window = Tk()
window.title("任务列表生成器")
window.geometry("400x300")

tasklist = []

def hit_b1():
    
    with open('C:\\Users\Wargon\Desktop\任务列表.txt','r') as  f:
        i = 0 #i必须有初始值
        while(i!=''):
            i = f.readline().strip() #除掉奇怪的符号
            if i != '': #如果i不是一个空行
                tasklist.append(i)
            
        shuffle(tasklist) #打乱排序
        for i in range(len(tasklist)):
            tasklist[i] = str(i+1)+'.'+tasklist[i] #给任务编号
            
        var.set(tasklist)

b1= Button(window,text="生成",width=10,height=2,command=hit_b1)

var = StringVar()

lb = Listbox(window,listvariable=var)

L1 = Label(window,text="让我们来加点任务吧")

b1.pack()
lb.pack()

window.mainloop()
