from options import Options

class Question:

    guess: str = None

    def __init__(self, text: str, correct_answer: str, options: Options):
        self.text = text
        self.correct_answer = correct_answer
        self.options = options

    def __str__(self) -> str:
        return f"{self.text}"
    
    def set_guess(self, guess: str):
        self.guess = guess.upper()

    def get_last_answer(self):
        return self.correct_answer == self.guess