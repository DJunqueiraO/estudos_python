from tkinter import *
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 200

SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "#ff0000"
BACKGROUND_COLOR = "#000000"

CONTROL_KEYS = {
    "w": "up",
    "a": "left",
    "s": "down",
    "d": "right",
    "Up": "up",
    "Left": "left",
    "Down": "down",
    "Right": "right"
}

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, 
                y, 
                x + SPACE_SIZE, 
                y + SPACE_SIZE, 
                fill=SNAKE_COLOR, 
                tag="snake"
            )
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH/SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT/SPACE_SIZE) - 1)) * SPACE_SIZE
        self.coordinates = (x, y)

        canvas.create_oval(
            x, 
            y, 
            x + SPACE_SIZE, 
            y + SPACE_SIZE, 
            fill=FOOD_COLOR, 
            tag="food"
        )

def next_turn(snake: Snake, food: Food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, 
        y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE_COLOR
    )
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.configure(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else: 
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(event: Event):
    global direction

    new_direction = CONTROL_KEYS.get(event.keysym)

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake: Snake):
    x, y = snake.coordinates[0]

    if x >= GAME_WIDTH - SPACE_SIZE:
        snake.coordinates[0] = - SPACE_SIZE, y
    elif x < 0:
        snake.coordinates[0] = GAME_WIDTH, y
    elif y < 0:
        snake.coordinates[0] = x, GAME_HEIGHT
    elif y >= GAME_HEIGHT - SPACE_SIZE:
        snake.coordinates[0] = x, - SPACE_SIZE

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def game_over():
    label.configure(text="Game over!")

window = Tk()
window.title("Python Game")
window.resizable(False, False)

score = 0

direction = "down"

label = Label(window)
label.configure(
    text="Score: {}".format(score), 
    font=("Consolas", 40)
)
label.pack()

canvas = Canvas(window)
canvas.configure(
    bg=BACKGROUND_COLOR, 
    height=GAME_HEIGHT, 
    width=GAME_WIDTH
)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
window.bind("<Key>", change_direction)

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()