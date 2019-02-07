import tkinter as tk
from tkinter import messagebox
import pickle

window = tk.Tk()
window.title('Welcome')
window.geometry('500x300')

#welcome image
canvas = tk.Canvas(window,height=200,width=500)

canvas.pack(side='top')

#user information
tk.Label(window,text='User name: ').place(x=50,y=150)
tk.Label(window,text='Password: ').place(x=50,y=200)

var_usr_name = tk.StringVar()
var_usr_name.set('example')
entry_usr_name = tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
var_usr_pwd= tk.StringVar()
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=200)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file) #usrs_info 是用户信息Users Information
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info=  {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome',message='Hi '+usr_name)
        else:
            tk.messagebox.showerror(message='Error,you password is wrong,try again')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                            'You have not sign up yet.Sign up today?')
        if is_sign_up:
            usr_sign_up()
    
def usr_sign_up():
    def sign_to_mofan():
        np = new_pwd.get() #新建密码
        npf = new_pwd_confirm.get() #新建确认密码
        nn= new_name.get() #新建用户名
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file) #用户信息
        if np != npf: #如果密码和确认密码不一致
            tk.messagebox.showerror('Error','Password and confirm password must be the same!')
        elif nn in exist_usr_info: #数据里已经有这个用户名
            tk.messagebox.showerror('Error','The user has already sign up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
                tk.messagebox.showinfo('Welcome','You have successfully signed up!')
                window_sign_up.destroy()
                
    window_sign_up =  tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example')
    tk.Label(window_sign_up,text='User name: ').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='Password: ').place(x=10,y=50)
    entry_usr_pwd = tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_usr_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text='Confirm password: ').place(x=10,y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_usr_pwd_confirm.place(x=150,y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up,text='Sing up',command=sign_to_mofan)
    btn_comfirm_sign_up.place(x=150,y=130)
            
#login and sign up button
btn_login = tk.Button(window,text='login',command=usr_login)
btn_login.place(x=170,y=230)
btn_sign_up = tk.Button(window,text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=270,y=230)

window.mainloop()
