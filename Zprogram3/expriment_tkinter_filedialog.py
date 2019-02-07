import tkinter as tk
import tkinter.filedialog

a = tk.filedialog.asksaveasfilename() #直接打开就是了，连master都不需要
print(a)
