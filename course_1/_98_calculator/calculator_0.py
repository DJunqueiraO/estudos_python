from tkinter import *
from calculator_button import *

def button_press(button_text: str):
    print(button_text)

def equals():
    pass

def clear():
    pass

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window)
label.configure(
    textvariable=equation_label,
    font=('consolas', 20),
    background='white',
    width=24,
    height=2
)
label.pack()

frame = Frame(window)
frame.pack()

button = CalculatorButton(frame).configure(
    command=lambda: button_press('1')
)
button.grid(row=0, column=0)

window.mainloop()