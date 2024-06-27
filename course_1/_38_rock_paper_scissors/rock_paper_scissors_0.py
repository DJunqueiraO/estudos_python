from choices import choice
import random

ROCK: str = 'rock'
PAPER: str = 'paper'
SCISSORS: str = 'scissors'

win_dictionary: dict = {
    ROCK : choice(SCISSORS, 'rock smashes scissors!!'), 
    PAPER : choice(ROCK, 'paper covers rock!!', ), 
    SCISSORS : choice(PAPER,'scissors cuts paper!!')
}

computer: str = random.choice(list(win_dictionary.keys()))
player: str = None

while player not in list(win_dictionary.keys()):
    player = input(f'{ROCK}, {PAPER} or {SCISSORS}? ').lower()

print(f'player: {player}')
print(f'computer: {computer}')

if(player == computer):
    print('it\'s a tie!')
    
result: choice = win_dictionary[player]
if result == computer:
    print('player wins!', end=' ')
else:
    print('computer wins!', end=' ')
print(result.winPhrase)