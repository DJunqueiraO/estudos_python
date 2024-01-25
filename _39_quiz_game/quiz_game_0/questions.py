from options import Options

class Question:

    last_answer = False

    def __init__(self, text: str, correct_answer: str, options: Options):
        self.text = text
        self.correct_answer = correct_answer
        self.options = options

    def __str__(self) -> str:
        return f"{self.text}"
    
    def set_answer(self, guess: str):
        self.last_answer = self.correct_answer == guess.upper()

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

    def get_correct_answers(self) -> list[str]:
        correct_answers = []
        for question in self:
            if question.last_answer:
                correct_answers.append(question.correct_answer)
            
        return correct_answers
    