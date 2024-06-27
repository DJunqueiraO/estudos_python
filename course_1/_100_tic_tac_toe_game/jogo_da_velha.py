from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == '' and check_winner() is False:
        buttons[row][column]['text'] = player
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.configure(text=f'{players[1]} turn')
            elif check_winner() is True:
                label.configure(text=f'{players[0]} wins')
            elif check_winner() == 'Tie':
                label.configure(text='Tie')
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.configure(text=f'{players[0]} turn')
            elif check_winner() is True:
                label.configure(text=f'{players[1]} wins')
            elif check_winner() == 'Tie':
                label.configure(text='Tie')
            

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].configure(background='green')
            buttons[row][1].configure(background='green')
            buttons[row][2].configure(background='green')
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].configure(background='green')
            buttons[1][column].configure(background='green')
            buttons[2][column].configure(background='green')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].configure(background='green')
        buttons[1][1].configure(background='green')
        buttons[2][2].configure(background='green')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].configure(background='green')
        buttons[1][1].configure(background='green')
        buttons[2][0].configure(background='green')
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].configure(background='yellow')
        return 'Tie'
    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    return spaces != 0

def new_game():
    global player

    player = random.choice(players)

    label.configure(text=f'{player} turn')

    for row in range(3):
        for column in range(3):
            buttons[row][column].configure(text='', background='#f0f0f0')

window = Tk()
window.title('Tic Tac Toe/Jogo da Velha')
players = ['X', 'O']
player = random.choice(players)
buttons: list[list[Button]] = [
    [None, None, None], 
    [None, None, None], 
    [None, None, None]
]

label = Label(
    text=player + ' turn', 
    font=('consolas', 40)
)
label.pack(side=TOP)

reset_button = Button(window)
reset_button.configure(
    text='restart',
    font=('consolas', 20),
    command=new_game
)
reset_button.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        button = Button(frame)
        button.configure(text='', 
            font=('consolas', 40), 
            width=5, 
            height=2,
            command=lambda row=row, col=col: next_turn(row, col)
        )
        button.grid(row=row, column=col)
        buttons[row][col] = button

window.mainloop()