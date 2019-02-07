from tkinter import * #导入的了message，导入不了messagebox的方法
from tkinter import messagebox #必须单独导入

window= Tk()
window.title('测试')
window.geometry('400x300')

def hit_b1():
    #messagebox.showinfo(title='Hi',message='Hahhh')
    #messagebox.showwarning(title='Hi',message='Noooo!')
    #messagebox.showerror(title='Hi',message='No!ever')
    #print(messagebox.askquestion(title='Hi',message='hahhh'))
    #return 'yes' or 'no'
    #print(messagebox.askyesno(title='Hi',message='hahhh'))
    #return 'True' or 'False'
    #print(messagebox.askretrycancel(title='Hi',message='hahhhh'))
    #choice:'重试' or '取消' return 'True' or 'False'
    print(messagebox.askokcancel(title='Hi',message='hahhh'))

b1= Button(window,text='hit me',command=hit_b1).pack()

window.mainloop()
