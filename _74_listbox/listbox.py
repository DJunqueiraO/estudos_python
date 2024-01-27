from tkinter import *

window = Tk()
# window.geometry('500x300')
window.state('zoomed')

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

window.mainloop()