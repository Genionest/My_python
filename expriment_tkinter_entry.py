import tkinter as tk

window = tk.Tk()
window.title('测试')

e= tk.Entry(window,show=None)

def hit_b():
    print(type(e.get()))

b = tk.Button(window,text='print',command=hit_b)

e.pack()
b.pack()

window.mainloop()
