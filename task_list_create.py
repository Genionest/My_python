from tkinter import Tk,Button,Listbox,StringVar,Label,Toplevel
from random import shuffle
from PIL import Image,ImageTk

window = Tk()
window.title("任务列表生成器")
window.geometry("400x300")

tasklist = []
img = Image.open('img\\20180912111525828.jpg')
photo = ImageTk.PhotoImage(img)

def hit_b1():
    
    with open('C:\\Users\Wargon\Desktop\任务列表.txt','r') as  f:
        i = 0
        while(i!=''):
            i = f.readline().strip()
            if i != '': 
                tasklist.append(i)
            
        shuffle(tasklist) 
        for i in range(len(tasklist)):
            tasklist[i] = str(i+1)+'.'+tasklist[i]+++++++++++++++
            
        var.set(tasklist)

        #window_list= Toplevel(window)
        #window_list.geometry('500x600')
        #window_list.title('任务列表')

        #list_var = StringVar()
        #list_str = "".join(tasklist)
        #list_var.set(list_str)
        
        #Label(window_list,image=photo,textvariable=list_var).pack()
        #字符串会被Label挡住

b1= Button(window,text="生成",width=10,height=2,command=hit_b1)

var = StringVar()

lb = Listbox(window,listvariable=var)

L1 = Label(window,text="让我们来加点任务吧")

b1.pack()
lb.pack()

window.mainloop()

