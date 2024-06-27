from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

def change_color():
    color = colorchooser.askcolor(title="pick a color")
    text.configure(foreground=color[1])

def change_font(*args):
    text.configure(font=(font_name.get(), size_box.get()))
    
def new_file():
    window.title('Untitled')
    text.delete(1.0, END)

def open_file():
    file = askopenfilename(
        initialdir=THIS_DIR,
        defaultextension=".txt", 
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
    )
    if file == '':
        return
    try:
        window.title(os.path.basename(file))
        text.delete(1.0, END)
        file = open(file, 'r')
        text.insert(1.0, file.read())
    except FileExistsError:
        print("Couldn't read file")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(
        initialdir=THIS_DIR,
        initialfile="untitled.txt",
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
    )
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')
            file.write(text.get(1.0, END))
        except FileExistsError:
            print("Couldn't write file")
        finally:
            file.close()

def cut():
    text.event_generate('<<Cut>>')

def copy():
    text.event_generate('<<Copy>>')

def paste():
    text.event_generate('<<Paste>>')

def about():
    showinfo(
        'About this program', 
        'This is a program created by djunqueirao'
    )

def quit():
    window.destroy()

window = Tk()
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

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text = Text(window)
text.configure(
    font=(font_name.get(), font_size.get())
)
scroll_bar = Scrollbar(text)
scroll_bar.pack(side=RIGHT, fill=Y)
text.configure(yscrollcommand=scroll_bar.set)
text.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame)
color_button.configure(text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(
    frame,
    font_name, 
    *font.families(), 
    command=change_font
)
font_box.grid(row=0, column=1)

size_box = Spinbox(
    frame, 
    from_=1, to=100, 
    textvariable=font_size, 
    command=change_font
)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.configure(menu=menu_bar)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.mainloop()