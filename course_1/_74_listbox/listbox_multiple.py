from tkinter import *
from typing import Callable

class SubmitButton(Button):
    def __init__(self, window):
        super().__init__(window)
        self.pack(side=LEFT)

    def setText(self, text: str):
        self.configure(text=text)

    def setSubmit(self, listbox: Listbox):
        def submit():
            food = list(map(lambda index: listbox.get(index), listbox.curselection()))
            print(f"You have ordered: {', '.join(food)}")
        self.configure(command=submit)

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

listbox.configure(
    height=listbox.size(),
    selectmode=MULTIPLE
)

entryBox = Entry(window)
entryBox.pack(fill=X)

buttonsFrame = Frame(window)
buttonsFrame.pack()

submitButton = SubmitButton(buttonsFrame)
submitButton.setText('Submit')
submitButton.setSubmit(listbox)

addButton = Button(buttonsFrame)
addButton.configure(
    text='add',
    command=lambda: (listbox.insert(listbox.size(), entryBox.get()), listbox.configure(height=listbox.size()))
)
addButton.pack(side=LEFT)

def delete():
    if listbox.curselection() == None:
        return

    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.configure(height=listbox.size())
deleteButton = Button(buttonsFrame)
deleteButton.configure(
    text='delete',
    command=delete
)
deleteButton.pack(side=LEFT)

window.mainloop()