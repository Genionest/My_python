import tkinter as tk
from PIL import Image,ImageTk

window = tk.Tk()
window.geometry('1200x1300')
window.title('test')

img = Image.open('img\\20180912111525828.jpg') #两条杠就行了
photo = ImageTk.PhotoImage(img)
tk.Label(window,image=photo).pack()

window.mainloop()
