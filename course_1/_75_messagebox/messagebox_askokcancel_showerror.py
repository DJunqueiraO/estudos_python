from tkinter import *
from tkinter import messagebox

window = Tk()

def goToHellForever():
    if not messagebox.askokcancel(title='askokcancel', message='You want to go to hell?'):
        return
    while True:
        messagebox.showerror(title='Error', message='Go to Hell!')
        
button = Button(window)
button.configure(
    text='click me', 
    command=goToHellForever
)
button.pack()

window.mainloop()