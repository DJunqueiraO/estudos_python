from tkinter import *
from tkinter import messagebox

window = Tk()

def buttonCommand():
    answer = messagebox.askyesnocancel(
        title='ask yes no cancel', 
        message='Do you are you?',
        icon='info'
    )
    if answer == True:
        print('I am you')
    elif answer == False:
        print('You are me')
    else:
        print('I do not know')
      
button = Button(window)
button.configure(
    text='click me', 
    command=buttonCommand
)
button.pack()

window.mainloop()