from tkinter import *
from tkinter import filedialog

window = Tk()

print(__file__)

def saveAFile():
    file = filedialog.asksaveasfile(
        initialdir=__file__.replace(__file__.split("\\")[-1], ""),
        defaultextension=".txt", 
        filetypes=[
            ('Text files', '.txt'),
            ('HTML files', '.html')
        ]
    )
    if file is None:
        return
    fileText = input('Enter your text: ')
    fileText and file.write(fileText)
    file.close()
    
button = Button(window)
button.configure(
    text="Save File", 
    command=saveAFile,
    background="green",
    foreground="honeydew"
)
button.pack()

window.mainloop()