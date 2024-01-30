from tkinter import *
from tkinter import font
from tkinter.messagebox import *
from tkinter.filedialog import *

from text_editor import *
from size_box import *
from font_box import *
from text_editor_window import *
from file_menu import *

def about():
    showinfo(
        'About this program', 
        'This is a program created by djunqueirao'
    )

window = TextEditorWindow()
window.title('Text Editor Program')

file = None

THIS_DIR = __file__.replace(__file__.split('\\')[-1], "")

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (WINDOW_WIDTH / 2)
y = (screen_height / 2) - (WINDOW_HEIGHT / 2) 

window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, int(x), int(y)))

text = TextEditor(window)
scroll_bar = Scrollbar(text)
scroll_bar.pack(side=RIGHT, fill=Y)
text.configure(yscrollcommand=scroll_bar.set)
text.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame)
color_button.configure(text="color", command=text.change_color)
color_button.grid(row=0, column=0)

font_box = FontBox(frame, text_editor=text)
font_box.grid(row=0, column=1)

size_box = SizeBox(frame, text_editor=text)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)

file_menu = FileMenu(
    menu_bar, 
    initialdir=THIS_DIR,
    text_editor=text
)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=text.cut)
edit_menu.add_command(label="Copy", command=text.copy)
edit_menu.add_command(label="Paste", command=text.paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.configure(menu=menu_bar)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.mainloop()