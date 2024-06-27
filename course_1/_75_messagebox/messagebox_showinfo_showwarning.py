from tkinter import *
from tkinter import messagebox

window = Tk()
        
button = Button(window)
button.configure(
    text='click me', 
    command=lambda: (
        messagebox.showinfo(title='Info', message='You are He-Man'),
        messagebox.showwarning(title='Warning', message='You have the power'),
    )
)
button.pack()

window.mainloop()