from tkinter import *

window = Tk()

Button(
    window, 
    text='create new window',
    command=lambda: Toplevel()
)\
    .pack()

window.mainloop()