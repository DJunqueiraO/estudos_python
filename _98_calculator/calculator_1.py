from tkinter import *

def button_press(button_text: str):
    if button_text == '=':
        equals()
        return
    global equation_text

    equation_text += button_text
    equation_label.set(equation_text)

def equals():
    
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Cannot divide by 0!")
        equation_text = ''
    except SyntaxError:
        equation_label.set("Invalid syntax!")
        equation_text = ''

def clear():
    
    global equation_text
    equation_label.set("")
    equation_text = ''

window = Tk()
window.title("Calculator")

equation_text = ""
equation_label = StringVar()
button_cnf = {
    "height": 4, 
    "width": 9, 
    "font": 35
}

label = Label(window)
label.configure(
    textvariable=equation_label,
    font=('consolas', 20),
    background='black',
    foreground='#00ff00',
    width=24,
    height=2
)
label.pack()

frame = Frame(window)
frame.pack()

buttons = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['0', '.', '=', '/']
]
for line in range(len(buttons)):
    for column in range(len(buttons[line])):
        button = Button(frame)
        button.configure(button_cnf)
        button.configure(
            text=buttons[line][column],
            command=lambda line=line, column=column: button_press(buttons[line][column])
        )
        button.grid(row=line, column=column)

clear_button = Button(window)
clear_button.configure(button_cnf)
clear_button.configure(
    text='C',
    command=clear
)
clear_button.pack(fill=X)

window.mainloop()