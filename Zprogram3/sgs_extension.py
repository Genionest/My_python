from tkinter import *
import os
from webbrowser import open as browseropen
from requests import get
#H:\Qsanguosha 2018\extensions
#H:\sgskf三国杀开发
#H:\Qsanguosha-2018\QSanguosha.exe
window = Tk()
window.title("三国杀开发工具")
window.geometry('300x200')

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)

def hit_sgs():
    os.startfile(r'H:\Qsanguosha-2018')
def hit_kf():
    os.startfile(r"H:\sgskf三国杀开发")

def hit_card():
    os.startfile(r'C:\Users\wargon\Pictures\card')
def hit_full():
    os.startfile(r'C:\Users\wargon\Pictures\full')

def hit_code():
    browseropen(get(r'https://github.com/Mogara/QSanguosha-v2').url)
def hit_skill():
    browseropen(get(r'https://github.com/DGAH/LuaSkillsForQSGS').url)
    
b1 = Button(f1,text="三国杀",command=hit_sgs)
b2 = Button(f1,text='开发',command=hit_kf)
b3 = Button(f2,text='卡牌',command=hit_card)
b4 = Button(f2,text='全身像',command=hit_full)
b5 = Button(f3,text='源码',command=hit_code)
b6 = Button(f3,text='技能',command=hit_skill)

l1 = Label(f1,text="文件区",bg="green",font=('Arial',12))
l2 = Label(f2,text="图音区",bg="red",font=('Arial',12))
l3 = Label(f3,text="代码区",bg="blue",font=('Arial',12))

f1.grid(row=1,column=1,padx=10,pady=10)
f2.grid(row=1,column=2,padx=10,pady=10)
f3.grid(row=1,column=3,padx=10,pady=10)

l1.grid(row=1,column=1,padx=10,pady=10)
b1.grid(row=2,column=1,padx=10,pady=10)
b2.grid(row=3,column=1,padx=10,pady=10)

l2.grid(row=1,column=1,padx=10,pady=10)
b3.grid(row=2,column=1,padx=10,pady=10)
b4.grid(row=3,column=1,padx=10,pady=10)

l3.grid(row=1,column=1,padx=10,pady=10)
b5.grid(row=2,column=1,padx=10,pady=10)
b6.grid(row=3,column=1,padx=10,pady=10)

window.mainloop()
