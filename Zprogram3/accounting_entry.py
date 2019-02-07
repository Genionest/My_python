from tkinter import *

window = Tk()
window.title("会计分录")
window.geometry("300x200")

L1 = Label(window,text="借")
L2 = Label(window,text="贷")
e1 = Entry(window,width=10)
e11 = Entry(window,width=10)
e2 = Entry(window,width=10)
e22 = Entry(window,width=10)

def hit_b1():
    print("借："+e1.get()+'\t'+e11.get())
    e1.delete(0,END)
    e11.delete(0,END)
    
def hit_b2():
    print("  贷："+e2.get()+'\t  '+e22.get())
    e2.delete(0,END)
    e22.delete(0,END)
    

b1 = Button(window,text="借方录入",command=hit_b1)
b2 = Button(window,text='贷方录入',command=hit_b2)

L1.place(x=100,y=50,anchor='center')
L2.place(x=200,y=50,anchor='center')
e1.place(x=100,y=80,anchor='center')
e11.place(x=100,y=105,anchor='center')
e2.place(x=200,y=80,anchor='center')
e22.place(x=200,y=105,anchor='center')
b1.place(x=100,y=150,anchor='center')
b2.place(x=200,y=150,anchor='center')

window.mainloop()
