from tkinter import *
from time import *

def update():
    time_string = strftime('%I:%M:%S %p')
    time_label.configure(text=time_string)
    
    day_string = strftime('%A')
    day_label.configure(text=day_string)
    
    date_string = strftime('%B %d, %Y')
    date_label.configure(text=date_string)

    window.after(1000, update)

window = Tk()
window.configure(
    background='black'
)

time_label = Label(window)
time_label.configure(
    font=('Arial', 50),
    foreground='#00ff00',
    background='black'
)
time_label.pack()

day_label = Label(window)
day_label.configure(
    font=('Ink Free', 50),
    foreground='white',
    background='black'
)
day_label.pack()

date_label = Label(window)
date_label.configure(
    font=('Ink Free', 50),
    foreground='white',
    background='black'
)
date_label.pack()

update()

window.mainloop()