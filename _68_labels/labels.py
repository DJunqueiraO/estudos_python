from tkinter import *

window = Tk()
window.configure(background="#222222")

madruguinha = PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'madruguinha.png'))

label = Label(window, 
              text="Toma!!", 
              font=('Arial', 50, 'bold'), 
              fg="white", 
              bg="#222222", 
              relief=SUNKEN, 
              bd=10,
              padx=20,
              pady=20,
              image=madruguinha,
              compound='bottom')
# label.place(x=50, y=50)
label.pack()

window.mainloop()