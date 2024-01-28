from tkinter import *
from tkinter import filedialog

window = Tk()

button = Button(window)
def button_command():
    filePath = filedialog.askopenfilename(
        initialdir=__file__.replace(__file__.split('\\')[-1], ''),
        title='open a file, ok?',
        filetypes=(
            ('text files', '*.txt'),
            ('all files', '*.*')
        )
    )
    file = open(filePath, 'r')
    file.close()
button.configure(
    text='submit',
    command=button_command
)
button.pack()

window.mainloop()