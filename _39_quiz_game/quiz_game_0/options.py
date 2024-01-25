class Options:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"A: {self.a}\nB: {self.b}\nC: {self.c}\nD: {self.d}"