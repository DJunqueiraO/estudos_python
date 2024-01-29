from tkinter import *
from dragger import *

window = Tk()

dragger = Dragger(window)

label_1 = Label(window)
label_1.configure(
    background='red',
    width=10,
    height=5
)
label_1.place(x=0, y=0)
label_1.bind('<Button-1>', dragger.drag_start)
label_1.bind('<B1-Motion>', dragger.drag_motion)

label_2 = Label(window)
label_2.configure(
    background='blue',
    width=10,
    height=5
)
label_2.place(x=20, y=50)
label_2.bind('<Button-1>', dragger.drag_start)
label_2.bind('<B1-Motion>', dragger.drag_motion)

window.mainloop()