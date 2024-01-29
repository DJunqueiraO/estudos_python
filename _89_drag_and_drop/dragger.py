from tkinter import *

class Dragger():

    def __init__(self, default_root: Tk):
        self.draggingPositionX = IntVar()
        self.draggingPositionY = IntVar()

    def drag_start(self, event: Event):
        self.draggingPositionX.set(event.x)
        self.draggingPositionY.set(event.y)

    def drag_motion(self, event: Event):
        widget: Label = event.widget
        x = widget.winfo_x() - self.draggingPositionX.get() + event.x
        y = widget.winfo_y() - self.draggingPositionY.get() + event.y
        widget.place(x=x, y=y)