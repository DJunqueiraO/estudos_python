from tkinter import colorchooser
from tkinter import *

window = Tk()

window.geometry("420x420")

button = Button(window)
button.configure(
    text='Click me',
    command=lambda: (
        window.configure(background=colorchooser.askcolor()[-1])
    )
)
button.pack() 

window.mainloop()