from win32api import RegOpenKey,RegSetValueEx,RegCloseKey
from win32con import HKEY_LOCAL_MACHINE,KEY_ALL_ACCESS,REG_SZ
from tkinter import Tk,Label,StringVar,Entry,Button
#设置初始路径，值，变量名
dir_proxy_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor"
value = "Intel(R) Core(TM) i7-4710MQ CPU @ 2.50GHz"
value_name = 'ProcessorNameString'

window = Tk()
window.title("CPU修改器")
window.geometry("400x300")

L1 = Label(window,text="请问你是管理员吗",font=("Arial",12),width=15,height=3)
var = StringVar()
e = Entry(window,show=None,textvariable=var,borderwidth=5,width=40)
var.set(value)

def hit_b1():
    if e.get()!=0:
        for i in range(8):
            #路径变到8个线程都要
            proxy_path = dir_proxy_path+"\\"+str(i)
            new_value = e.get()
            #修改注册表
            key = RegOpenKey(HKEY_LOCAL_MACHINE,proxy_path,0,KEY_ALL_ACCESS)
            RegSetValueEx(key,value_name,0,REG_SZ,new_value)
            RegCloseKey(key)
    var.set(value) #设置回初始值

b1 = Button(window,text="修改",width=10,height=1,command=hit_b1)

L1.pack()
e.pack()
b1.pack()

window.mainloop()
