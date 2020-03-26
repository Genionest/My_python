from tkinter import *
import os
from webbrowser import open as browseropen
from requests import get
# F:\steam\steamapps\common\dont_starve\mods
# F:\steam\steamapps\common\dont_starve\data
# C:\Users\wargon\Documents\Klei\DoNotStarve
# F:\steam\steamapps\common\Don't Starve Mod Tools\mod_tools
# F:\jhkf
window = Tk()
window.title("饥荒开发工具")
window.geometry('300x200')

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)

def hit_mods():
    os.startfile(r"F:\steam\steamapps\common\dont_starve\mods")


def hit_data():
    os.startfile(r"F:\steam\steamapps\common\dont_starve\data")


def hit_log():
    os.startfile(r"C:\Users\wargon\Documents\Klei\DoNotStarve\log.txt")

    
def hit_tools():
    os.startfile(r"F:\steam\steamapps\common\Don't Starve Mod Tools\mod_tools")


def hit_spriter():
    os.startfile(r"F:\steam\steamapps\common\Don't Starve Mod Tools\mod_tools\Spriter")


def hit_auto():
    os.startfile(r"F:\steam\steamapps\common\Don't Starve Mod Tools\mod_tools\autocompiler.exe")


def hit_kf():
    os.startfile(r"F:\jhkf")


def hit_rezip():
    os.startfile(r"F:\jhkf\rezip")


def hit_code():
    os.startfile(r"F:\jhkf\jhcode.txt")


def hit_block():
    pass

b11 = Button(f1, text="mods", command=hit_mods)
b12 = Button(f1, text="data", command=hit_data)
b13 = Button(f1, text="log", command=hit_log)
b21 = Button(f2, text="tools", command=hit_tools)
b22 = Button(f2, text="spriter", command=hit_spriter)
b23 = Button(f2, text="auto", command=hit_auto)
b31 = Button(f3, text="开发", command=hit_kf)
b32 = Button(f3, text="解压", command=hit_rezip)
b33 = Button(f3, text="code", command=hit_code)

l1 = Label(f1,text="游戏文件",bg="green",font=('Arial',12))
l2 = Label(f2,text="工具区",bg="red",font=('Arial',12))
l3 = Label(f3,text="开发区",bg="blue",font=('Arial',12))

f1.grid(row=1,column=1,padx=10,pady=10)
f2.grid(row=1,column=2,padx=10,pady=10)
f3.grid(row=1,column=3,padx=10,pady=10)

l1.grid(row=1,column=1,padx=10,pady=10)
b11.grid(row=2,column=1,padx=10,pady=10)
b12.grid(row=3,column=1,padx=10,pady=10)
b13.grid(row=4,column=1,padx=10,pady=10)

l2.grid(row=1,column=1,padx=10,pady=10)
b21.grid(row=2,column=1,padx=10,pady=10)
b22.grid(row=3,column=1,padx=10,pady=10)
b23.grid(row=4,column=1,padx=10,pady=10)

l3.grid(row=1,column=1,padx=10,pady=10)
b31.grid(row=2,column=1,padx=10,pady=10)
b32.grid(row=3,column=1,padx=10,pady=10)
b33.grid(row=4,column=1,padx=10,pady=10)

window.mainloop()
