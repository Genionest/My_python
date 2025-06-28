import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()