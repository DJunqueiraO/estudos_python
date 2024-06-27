from tkinter import *
from typing import Callable

class CustomButton(Button):
    def __init__(self, window):
        super().__init__(window)
        self.pack(side=LEFT)

    def setText(self, text: str):
        self.configure(text=text)

    def setCommand(self, command: Callable):
        self.configure(command=command)

window = Tk()
# window.geometry('500x300')
# window.state('zoomed')

items = [
    'hamburger', 
    'hotdog', 
    'pizza', 
    'pasta', 
    'garlic bread'
]

listbox = Listbox(window)
for index in range(len(items)):
    listbox.insert(index, items[index])
listbox.configure(
    background='#f7ffde',
    font=('constantia', 18)
)
listbox.pack(fill=BOTH, expand=TRUE)

listbox.configure(height=listbox.size())

entryBox = Entry(window)
entryBox.pack(fill=X)

buttonsFrame = Frame(window)
buttonsFrame.pack()

submitButton = CustomButton(buttonsFrame)
submitButton.setText('Submit')
submitButton.setCommand(
    lambda: listbox.curselection() and print(listbox.get(listbox.curselection()))
)

addButton = Button(buttonsFrame)
addButton.configure(
    text='add',
    command=lambda: (listbox.insert(listbox.size(), entryBox.get()), listbox.configure(height=listbox.size()))
)
addButton.pack(side=LEFT)

deleteButton = Button(buttonsFrame)
deleteButton.configure(
    text='delete',
    command=lambda: listbox.curselection() and (listbox.delete(listbox.curselection()), listbox.configure(height=listbox.size()))
)
deleteButton.pack(side=LEFT)

window.mainloop()