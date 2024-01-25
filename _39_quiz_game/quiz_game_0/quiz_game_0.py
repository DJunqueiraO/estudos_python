from questions import Questions
from displayer import Displayer

quiz_questions = Questions()
quiz_displayer = Displayer(quiz_questions)

def new_game():
    correct_guesses = []

    for question in quiz_questions:
        quiz_displayer.print_line()
        print(question)
        print(question.options)
        
        guess = input("Enter (A, B, C, or D): ").upper()
        question.set_answer(guess)
        correct_guesses.append(guess)

    quiz_displayer.show_scorre(correct_guesses)

def play_again():
    response = input("do you want to play again? (yes or no): ")
    return response.upper() == "YES" or response.upper() == "Y"

while True:
    new_game()
    if not play_again():
        break