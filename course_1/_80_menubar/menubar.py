from tkinter import *

window = Tk()

menubar = Menu(window)

openImage = PhotoImage(file=__file__.replace(__file__.split("\\")[-1], "abrir.png"))
saveImage = PhotoImage(file=__file__.replace(__file__.split("\\")[-1], "salvar.png"))
exitImage = PhotoImage(file=__file__.replace(__file__.split("\\")[-1], "sair.png"))

menuDefaultCnf = {
    "tearoff": 0,
    "font": ("MV Boil", 15)
}

filemenu = Menu(menubar)
filemenu.configure(menuDefaultCnf)
filemenu.add_command(
    label='Open', 
    command=lambda: print('file open'),
    image=openImage, compound=LEFT
)
filemenu.add_command(
    label='Save',
    command=lambda: print('file save'),
    image=saveImage, compound=LEFT
)
filemenu.add_separator()
filemenu.add_command(
    label='Exit', 
    command=quit,
    image=exitImage, compound=LEFT
)

editMenu = Menu(menubar)
editMenu.configure(menuDefaultCnf)
editMenu.add_command(
    label='Cut', 
    command=lambda: print('You cut something')
)
editMenu.add_command(
    label='Copy', 
    command=lambda: print('You copy something')
)
editMenu.add_command(
    label='Paste', 
    command=lambda: print('You paste something')
)

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editMenu)

window.configure(menu=menubar)
window.mainloop()