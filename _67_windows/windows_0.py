from tkinter import *
import os

window = Tk() #Cria uma janela
window.geometry('500x300') #Define o tamanho da janela
window.title('Josicleison janela') #Define o ti?tulo da janela

banana = PhotoImage(file=f'{os.getcwd()}\\Estudos_Python\\_67_windows\\banana.png')
window.iconphoto(False, banana)

window.config(bg='#222222')

window.mainloop() #Executa a janela