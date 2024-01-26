from tkinter import *

window = Tk()

x = BooleanVar()

pao = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'pao.png'))

check = lambda: print("You agree!") if x.get() else print("You disagree!")
check_button = Checkbutton(window)
check_button.configure(text="I am a checkbox",
                       variable=x,
                       font=('Arial', 20),
                       foreground='red',
                       background='green',
                       activeforeground='red',
                       activebackground='yellow',
                       command=check,
                       padx=10,
                       pady=10,
                       image=pao,
                       compound='left')
check_button.pack()

window.mainloop()