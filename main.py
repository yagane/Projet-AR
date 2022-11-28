
from puissance4 import *

from tkinter import *
import tkinter as tk
import numpy as np
import time

# #Création de la fenêtre tkinter
# window = tk.Tk()
# window.geometry("700x600")
# # fond = tk.PhotoImage(file="fond_P4.png")
# # label1 = Label(window, image=fond)
# # label1.pack()
#
# hauteur = 600
# largeur = 700
# canvas = Canvas(window, width=largeur, height=hauteur, background='blue')
# for i in range (6) : #nombre de lignes
#     canvas.create_line(100*(i+1), 0, 100*(i+1), hauteur, width=5)
# for i in range (7) : #nombre de colonnes
#     canvas.create_line(0, 100*(i+1), largeur, 100*(i+1), width=5)
# canvas.pack()



P4 = Puissance4()
P4.print_board()




#nécessaire pour laisser la fenêtre ouverte
P4.mainloop()








