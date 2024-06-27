from tkinter import *

window = Tk()

tiileLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name: ", width=20, background="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last Name: ", background="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailNameLabel = Label(window, text="Email Name: ", background="blue", width=30).grid(row=3, column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()