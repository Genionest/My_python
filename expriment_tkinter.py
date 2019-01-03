import tkinter as tk

window = tk.Tk()
window.title('测试')
window.geometry('400x300')

e = tk.Entry(window,show=None)

def hit_b1():
    print(e.get())

b1 = tk.Button(window,text='print',command=hit_b1)

e.pack()
b1.pack()

window.mainloop()
