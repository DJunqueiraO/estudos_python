from tkinter import *
from tkinter import messagebox

window = Tk()

def buttonCommand():
    answer = messagebox.askyesnocancel(title='ask yes no cancel', message='Do you are you?')
    if answer == True:
        print('I am you')
        return
    if answer == False:
        print('You are me')
        return
    if answer == None:
        print('I do not know')
        return
      
button = Button(window)
button.configure(
    text='click me', 
    command=buttonCommand
)
button.pack()

window.mainloop()