from tkinter import *

VELOCITY = 5

def move_up(event: Event):
    canvas.move(5, 0, -5)

def move_left(event: Event):
    canvas.move(5, -5, 0)

def move_right(event: Event):
    canvas.move(5, 5, 0)

def move_down(event: Event):
    canvas.move(5, 0, 5)

root = Tk()
root.bind('<w>', move_up)
root.bind('<a>', move_left)
root.bind('<d>', move_right)
root.bind('<s>', move_down)
root.bind('<Up>', move_up)
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)
root.bind('<Down>', move_down)

demon = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'demon.png'))

canvas = Canvas(root)
canvas.configure(
    width=500,
    height=500
)
canvas.create_image(0, 0, image=demon, anchor=NW)
canvas.pack()

root.mainloop()