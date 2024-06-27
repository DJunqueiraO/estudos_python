from tkinter import *
from tkinter import messagebox

window = Tk()

def buttonCommand():
    answer = messagebox.askquestion(title='ask question', message='Do you like bread ???')

    if answer == 'yes':
        print('I like bread too.')
    else:
        print('Breads are perfect. :)')
      
button = Button(window)
button.configure(
    text='click me', 
    command=buttonCommand
)
button.pack()

window.mainloop()