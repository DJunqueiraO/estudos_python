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
    fileText = str(text.get('1.0', END))
    if file:
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

text = Text(window)
text.configure(
    {
        "background" : "pink",
        "foreground" : "teal",
        "font" : ("Arial", 15)
    }
)
text.pack()

window.mainloop()