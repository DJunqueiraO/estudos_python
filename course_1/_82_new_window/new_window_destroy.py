from tkinter import *

window = Tk()

Button(
    window, 
    text='create new window',
    command=lambda: (Tk(), window.destroy())
)\
    .pack()

window.mainloop()