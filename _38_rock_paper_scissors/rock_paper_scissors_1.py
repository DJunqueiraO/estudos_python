from choices import choice
import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

choices = [ROCK, PAPER, SCISSORS]

while True:
    computer: str = random.choice(choices)
    player: str = None

    while player not in choices:
        player = input(f'{ROCK}, {PAPER} or {SCISSORS}? ').lower()

    print(f'player: {player}')
    print(f'computer: {computer}')

    if player == computer:
        print('it\'s a tie!')
    elif player == PAPER and computer == ROCK:
        print(f'player wins! {PAPER} covers {ROCK}')
    elif player == SCISSORS and computer == PAPER:
        print(f'player wins! {SCISSORS} cut {PAPER}')
    elif player == ROCK and computer == SCISSORS:
        print(f'player wins! {ROCK} smashes {SCISSORS}')
    else:
        print('computer wins!')

    play_again = input('play again? (y/n) ').lower()
    if play_again != 'y':
        break

print('Bye!')