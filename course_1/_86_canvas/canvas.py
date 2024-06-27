from tkinter import *

window = Tk()

canvas = Canvas(window)
canvas.configure(width=500, height=500)
points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill="hotpink", width=5)
redLine = canvas.create_line(0, 0, 500, 500, fill="red", width=5)
blueLine = canvas.create_line(0, 500, 500, 0, fill="blue", width=5)
canvas.create_rectangle(50, 50, 250, 250, fill="purple", width=5, outline="gray")
canvas.create_arc(
    0, 0, 500, 500, fill="gray", style=PIESLICE, start=270, extent=180
)
canvas.pack()

window.mainloop()