class choice:
    def __init__(self, name: str, winPhrase: str = ''):
        self.name = name
        self.winPhrase = winPhrase

    def __str__(self) -> str:
        return self.name
