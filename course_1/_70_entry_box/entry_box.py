from tkinter import *
from multiprocessing import Process

def submit():
    global username
    username = entry.get()
    print(username)
    entry.configure(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

username = None

entry = Entry(window)
entry.configure(font=('monospace', 40),
                foreground='#00ff00',
                background='#0000ff',
                show='*')
entry.insert(0, 'spongebob')
entry.pack(side=LEFT)

submit_button = Button(window)
submit_button.configure(text='Submit',
                 command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window)
delete_button.configure(text='Delete',
                 command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window)
backspace_button.configure(text='Backspace',
                 command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()