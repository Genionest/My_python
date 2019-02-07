from tkinter import *

window= Tk()
window.title('Frame')
window.geometry('400x300')

frm = Frame(window)
frm.pack()
frm_L = Frame(frm,)
frm_r = Frame(frm)

frm_L.pack(side='left')
frm_r.pack(side='right')

Label(frm_L,text='on the frm_l1').pack(side='bottom')
Label(frm_L,text='on the frm_l2').pack(side='top')

Label(frm_r,text='on the frm_r').pack()

window.mainloop()
