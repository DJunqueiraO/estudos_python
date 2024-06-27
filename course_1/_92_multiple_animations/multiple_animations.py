from tkinter import *
import time
from ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window)
canvas.configure(
    width=WIDTH, 
    height=HEIGHT
)
canvas.pack()

volley_ball = Ball(canvas).configure(1, 1, 100, 1, 1, 'red')
tennis_ball = Ball(canvas).configure(1, 1, 50, 4, 3, 'yellow')
basket_ball = Ball(canvas).configure(1, 1, 125, 8, 7, 'orange')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()