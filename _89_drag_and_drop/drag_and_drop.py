from tkinter import *

def drag_start(event: Event):
    draggingPositionX.set(event.x)
    draggingPositionY.set(event.y)

def drag_motion(event: Event):
    widget: Label = event.widget
    x = widget.winfo_x() - draggingPositionX.get() + event.x
    y = widget.winfo_y() - draggingPositionY.get() + event.y
    widget.place(x=x, y=y)

window = Tk()

draggingPositionX = IntVar()
draggingPositionY = IntVar()

label_1 = Label(window)
label_1.configure(
    background='red',
    width=10,
    height=5
)
label_1.place(x=0, y=0)
label_1.bind('<Button-1>', drag_start)
label_1.bind('<B1-Motion>', drag_motion)

label_2 = Label(window)
label_2.configure(
    background='blue',
    width=10,
    height=5
)
label_2.place(x=20, y=50)
label_2.bind('<Button-1>', drag_start)
label_2.bind('<B1-Motion>', drag_motion)

window.mainloop()