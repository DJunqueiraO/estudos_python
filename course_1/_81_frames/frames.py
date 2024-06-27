from tkinter import *

root = Tk()

class MyButton(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.configure(
            font=("consolas", 25),
            width=3
        )

frame = Frame(root)
frame.configure(
    background="pink",
    border=5,
    relief=SUNKEN
)
# frame.pack(anchor=CENTER, expand=TRUE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

MyButton(frame, text="w").pack(side=TOP)
MyButton(frame, text="a").pack(side=LEFT)
MyButton(frame, text="s").pack(side=LEFT)
MyButton(frame, text="d").pack(side=LEFT)

root.mainloop()