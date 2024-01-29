from tkinter import *

window = Tk()

canvas = Canvas(window)
canvas.configure(width=500, height=500)

canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10)
canvas.create_arc(0,0,500,500,fill='white',extent=180,width=10,start=180)
canvas.create_oval(190,190,310,310,fill='white',width=10)

canvas.pack()

window.mainloop()