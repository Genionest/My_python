#一键打开日常

from tkinter import Tk,Label,Button,Entry,StringVar,Listbox,END,messagebox
from requests import get
from webbrowser import open as browseropen

#读取需要打开的网页
def get_web_list():
    with open('D:\python3.6.1\Zprogram3\day_done.txt','r') as f:
        i=0
        lst=[]
        while(i!=''):
            i=f.readline().strip()
            lst.append(i)#最后一项是''，在网页打开时会出错
        lst.pop()
    return lst
#rlist是不带\n的网址列表
rlist = get_web_list()

#打开网页
def wopen():
    #webbrowser.open(r.url)
    try: #带上错误处理
        for i in rlist:
            browseropen(get(i).url)
    except Exception as error:
        #print('exception:',e)
        messagebox.showerror(title='错误',
                             message='网页无法解析!\n错误类型：'+str(error))
    finally:
        print('...')

window = Tk()
window.title('日常任务一键开启')
window.geometry('400x300')

l = Label(window,text='今天的日常好像还没做呢',font=('Arial',10),width=20,
            height=3)#width，height的长度都是根据字符的大小来定的

def hit_b1():
    wopen()

b1 = Button(window,text='开启',width=10,height=1,command=hit_b1)

e = Entry(window,show=None)

def hit_b2():
    with open('D:\python3.6.1\Zprogram3\day_done.txt','a') as f:
        if e.get()!='':
            f.write(e.get()+'\n')
            rlist.append(e.get())
            var.set(rlist)#重置目录
            e.delete(0,END)
    
b2 = Button(window,text='添加',width=10,height=1,command=hit_b2)

def hit_b3():
    value = lb.get(lb.curselection())
    rlist.remove(value)
    var.set(rlist)#重置目录
    #写删除后的文件
    with open('D:\python3.6.1\Zprogram3\day_done.txt','w') as f:
        for i in rlist:
            f.write(i+'\n')
            
b3 = Button(window,text='删除',width=10,height=1,command=hit_b3)

var = StringVar()
var.set(rlist)

lb = Listbox(window,listvariable=var)

#布局
l.pack()
b1.pack()
e.pack()
b2.pack()
b3.pack()
lb.pack()


window.mainloop()
