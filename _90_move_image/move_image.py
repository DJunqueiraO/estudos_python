from tkinter import *

VELOCITY = 5

def move_up(event: Event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - VELOCITY)

def move_down(event: Event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + VELOCITY)

def move_left(event: Event):
    label.place(x=label.winfo_x() - VELOCITY, y=label.winfo_y())

def move_right(event: Event):
    label.place(x=label.winfo_x() + VELOCITY, y=label.winfo_y())

root = Tk()
root.geometry("500x500")

demon = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'demon.png'))

label = Label(root)
label.configure(
    image=demon
)
label.place(x=0, y=0)

root.bind('<w>', move_up)
root.bind('<a>', move_left)
root.bind('<d>', move_right)
root.bind('<s>', move_down)

root.bind('<Up>', move_up)
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)
root.bind('<Bown>', move_down)

root.mainloop()