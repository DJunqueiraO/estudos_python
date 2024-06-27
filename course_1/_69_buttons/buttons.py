from tkinter import *



window = Tk()
window.configure(background="#222222")

button = Button(window)

count = 0

def click():
    global count
    count += 1
    print(f'lero lero, {count}')
    if count == 10:
        button.configure(state=DISABLED)

madruguinha = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'madruguinha.png'))

button.configure(text="Toma!!",
                 command=click,
                 font=("Comic Sans", 30),
                 background="#333333",
                 fg='white',
                 activeforeground='red',
                 activebackground='gray',
                 image=madruguinha,
                 compound='top')
button.pack()

window.mainloop()