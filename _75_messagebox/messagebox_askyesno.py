from tkinter import *
from tkinter import messagebox

window = Tk()

def buttonCommand():
    if messagebox.askyesno(title='ask yes no', message='Do you like cake?'):
        print('I like cake too')
    else:
        print('Why do you not like cake? Are you psyco?')
      
button = Button(window)
button.configure(
    text='click me', 
    command=buttonCommand
)
button.pack()

window.mainloop()