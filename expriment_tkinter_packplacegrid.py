import tkinter as tk

window= tk.Tk()
window.title('测试')
window.geometry('300x300')

tk.Label(window,text=123).place(x=20,y=100,anchor='center')
for i in range(3):
    for j in range(3):
        tk.Label(window,text=222).grid(row=i,column=j)

window.mainloop()
