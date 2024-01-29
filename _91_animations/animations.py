from tkinter import *
import time

WIDTH = 404
HEIGHT = 404
velocityX = 1.5
velocityY = 1

window = Tk()

TANK_PHOTOIMAGE = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'tank.png'))
BACKGROUND = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'bolo_de_chocolate.png'))

canvas = Canvas(window)
canvas.configure(
    width=WIDTH, 
    height=HEIGHT
)
background = canvas.create_image(0, 0, image=BACKGROUND, anchor=NW)
tank = canvas.create_image(0, 0, image=TANK_PHOTOIMAGE, anchor=NW)
canvas.pack()

image_width = TANK_PHOTOIMAGE.width()
image_height = TANK_PHOTOIMAGE.height()

while True:
    coordinates = canvas.coords(tank)
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        velocityX *= -1
    elif coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        velocityY *= -1
    window.update()
    canvas.move(tank, velocityX, velocityY)
    time.sleep(0.01)

window.mainloop()