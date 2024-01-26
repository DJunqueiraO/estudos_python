from tkinter import *

class Aplicativo(Tk):
    def __init__(self):
        super().__init__()

        frame = Frame(self)
        frame.configure(bg="blue")
        frame.pack(anchor="center", expand=TRUE, fill=BOTH)

        for i in range(3):
            label = Label(frame)
            label.configure(
                text=f"label: {i}", 
                background='red'
            )
            label.pack(side=LEFT)

        a = Label(frame)
        a.configure(
            text=f"label: {i}", 
            background='red'
        )
        a.pack(expand=TRUE, fill=BOTH)

        b = Label(frame)
        b.configure(
            text=f"label: {i}", 
            background='red'
        )
        b.pack(expand=TRUE, fill=BOTH)

if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()