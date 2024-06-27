from options import Options
from question import Question

QUESTION_1_OPTIONS = Options("Monty Python", "Guido van Rossum", "Rasmus Lerdorf", "Mark Pilgrim")
QUESTION_1 = Question("Who created Python? ", "B", QUESTION_1_OPTIONS)

QUESTION_2_OPTIONS = Options("1989", "1991", "2000", "2016")
QUESTION_2 = Question("What year was Python created? ", "B", QUESTION_2_OPTIONS)

QUESTION_3_OPTIONS = Options("Lonely Island", "Smosh", "Monty Python", "SNL")
QUESTION_3 = Question("Python is tributed to which comedy group? ", "C", QUESTION_3_OPTIONS)

QUESTION_4_OPTIONS = Options("True", "False", "Sometimes", "What's Earth?")
QUESTION_4 = Question("Is the Earth round? ", "A", QUESTION_4_OPTIONS)

class Questions(list[Question]):

    def __init__(self):
        super().__init__()
        self.append(QUESTION_1)
        self.append(QUESTION_2)
        self.append(QUESTION_3)
        self.append(QUESTION_4)

    def get_answers(self) -> list[str]:
        answers = []
        for question in self:
            answers.append(question.correct_answer)

        return answers
    
    def get_correct_guesses(self) -> list[str]:
        correct_guesses = []
        for question in self:
            if question.get_last_answer():
                correct_guesses.append(question.correct_answer)
            
        return correct_guesses
    
    def get_guesses(self):
        guesses = []
        for question in self:
            guesses.append(question.guess)
        
        return guesses