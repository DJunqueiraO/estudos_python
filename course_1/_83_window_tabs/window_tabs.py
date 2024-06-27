from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows

tab_1 = Frame(notebook) #new frame for tab 1
tab_2 = Frame(notebook) #new frame for tab 2

notebook.add(tab_1, text="Tab 1")
notebook.add(tab_2, text="Tab 2")
notebook.pack(expand=TRUE, fill=BOTH) #expand to fill root window and fill all space

Label(tab_1, text="Hello this is tab 1", width=50, height=25).pack()
Label(tab_2, text="Goodbye this is tab 2", width=50, height=25).pack()

window.mainloop()