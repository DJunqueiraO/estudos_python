def print_line():
    print("----------------------------------------")

def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print_line()
        print(key)
        for i in options[questions_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):

    print_line()
    print("RESULTS")
    print_line()

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print(f"Your score is {score}%")

def play_again():
    
    response = input("do you want to play again? (yes or no): ")
    return response.upper() == "YES"

questions = {
    "Who created Python? ": "B",
    "What year was Python created? ": "B", 
    "Python is tributed to which comedy group? ": "C", 
    "Is the Earth round? ": "A"
}

options = [
    ["A. Monty Python", "B. Guido van Rossum", "C. Rasmus Lerdorf", "D. Mark Pilgrim"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]
]

while True:
    new_game()
    if not play_again():
        break

print("Bye!")