from tkinter import *

window = Tk()

text = Text(window)
text.configure(
    {
        "background" : 'lightgreen',
        "font" : ('Ink Free', 25),
        "height" : 8,
        "width" : 25,
        "padx" : 20,
        "pady" : 20,
        "foreground" : 'blue'
    }
)
text.pack()

button = Button(window)
button.configure(
    text='submit',
    command=lambda: print(text.get('1.0', END)),
    background='red',
    foreground='white'
)
button.pack()

window.mainloop()