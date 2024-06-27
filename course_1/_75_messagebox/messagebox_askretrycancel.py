from tkinter import *
from tkinter import messagebox

window = Tk()

def buttonCommand():
    print('You retried a thing') if (
        messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry?')
    ) else print('You did not do a thing')
      
button = Button(window)
button.configure(
    text='click me', 
    command=buttonCommand
)
button.pack()

window.mainloop()