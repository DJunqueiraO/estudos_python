from questions import Questions
from functools import reduce

class Displayer:

    # __answers__ = None
    questions = None

    def __init__(self, questions: Questions):
        self.questions = questions

    def print_line(self):
        print("----------------------------------------")

    # def get_answers(self) -> list[str]:
    #     if self.__answers__ == None:
    #         self.__answers__ = list(map(lambda question: question.correct_answer, self.questions))
    #     return self.__answers__
    
    def show_scorre(self):
        self.print_line()
        print("RESULTS")
        print()
        print(f"Answers: {reduce(lambda a, b: a + " " + b, self.questions.get_answers())}")
        print(f"Guesses: {reduce(lambda a, b: a + " " + b, self.questions.get_guesses())}")
        print()

        correct_answers = self.questions.get_correct_guesses()
        score = int(len(correct_answers)/len(self.questions)*100)

        print(f"Your score is {score}%")
        
        self.print_line()