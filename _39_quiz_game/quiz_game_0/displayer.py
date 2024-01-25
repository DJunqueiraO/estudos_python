from questions import Questions
from functools import reduce

class Displayer:

    __guesses__ = None
    questions = None

    def __init__(self, questions: Questions):
        self.questions = questions

    def print_line(self):
        print("----------------------------------------")

    def get_guesses(self) -> list[str]:
        if self.__guesses__ == None:
            self.__guesses__ = list(map(lambda question: question.correct_answer, self.questions))
        return self.__guesses__
    
    def show_scorre(self, guesses: list[str]):
        self.print_line()
        print("RESULTS")
        print()
        print(f"Answers: {reduce(lambda a, b: a + " " + b, self.get_guesses())}")
        print(f"Guesses: {reduce(lambda a, b: a + " " + b, guesses)}")
        print()
        correct_answers = self.questions.get_correct_answers()
        score = int(len(correct_answers)/len(self.questions)*100)
        print(f"Your score is {score}%")
        self.print_line()