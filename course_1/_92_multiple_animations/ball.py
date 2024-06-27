from tkinter import Canvas

class Ball:
    def __init__(
            self, 
            canvas: Canvas, 
            x = 0, 
            y = 0, 
            diameter = 0, 
            xVelocity = 0, 
            yVelocity = 0, 
            color = ''
        ):
        self.canvas = canvas
        self.image = canvas.create_oval(
            x, y, x + diameter, y + diameter, fill=color
        )
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def configure(
        self,
        x = 0, 
        y = 0, 
        diameter = 0, 
        xVelocity = 0, 
        yVelocity = 0, 
        color = ''
    ):
        self.image = self.canvas.create_oval(
            x, y, x + diameter, y + diameter, fill=color
        )
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        return self
        

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] <= 0:
            self.xVelocity *= -1
        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] <= 0:
            self.yVelocity *= -1
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)