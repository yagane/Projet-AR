# -*- coding: utf-8 -*-
"""
Created on :
@author:
"""

from tkinter import *
import numpy as np

class Puissance4(Tk):

    def callback(self, event):
        #self.frame.focus_set()
        x = event.x
        x = int(x * self.column / self.width)
        self.play(x)
        if self.win:
            self.restart()


    def motion(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))

    def __init__(self):
        Tk.__init__(self)
        self.win = False
        self.column = 7
        self.line = 6
        self.width = 700
        self.height = 600
        self.player = 1
        self.board = None
        self.canvas = None
        self.reset()
        #Permet de resize les éléments quand on change la taille de la fenêtre
        #self.frame.pack()
        self.canvas.bind('<Button-1>', self.callback)
        self.canvas.pack()


    def reset(self):
        self.board = np.zeros((self.line, self.column))
        #self.frame = Frame(self, width=self.width, height=self.height)
        self.canvas = Canvas(self, width=self.width, height=self.height, background='blue')

    def restart(self):
        self.win = False
        self.player = 1
        self.board = np.zeros((self.line, self.column))
        self.canvas.delete("all")
        self.print_board()

    def possibles_plays(self):
        plays = []
        for i in range(self.column):
            for j in range(self.line):
                if self.board[self.line-j-1,i] == 0:
                    plays.append(self.line-j-1)
                    break
                elif j == self.line-1:
                    plays.append(-1)

        return plays

    def play(self, x):
        print("Player ", self.player ," doit jouer")

        if self.possibles_plays()[x] == -1:
            print("Ce coup n'est pas possible, rejouez !")
        else:
            self.board[self.possibles_plays()[x], x] = self.player

            self.check_win(self.possibles_plays()[x] + 1, x)

            self.print_board()

            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

    def check_win(self, x, y):

        if np.sum(self.board) == 63:
            print("Egalite")

        # On regarde si le joueur gagne en colonne
        if self.line-x >= 4:
            if self.board[x+1, y] == self.player and self.board[x+2, y] == self.player and self.board[x+3, y] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x <= 3:
            if self.board[x-1, y] == self.player and self.board[x-2, y] == self.player and self.board[x-3, y] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line - x >= 3 and x != 0:
            if self.board[x+1, y] == self.player and self.board[x+2, y] == self.player and self.board[x-1, y] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line - x <= 4 and x != self.line-1:
            if self.board[x-1, y] == self.player and self.board[x-2, y] == self.player and self.board[x+1, y] == self.player:
                print("player ", self.player ," win")
                self.win = True

        #On regarde si le joueur gagne en ligne
        if self.column-y >= 4:
            if self.board[x, y+1] == self.player and self.board[x, y+2] == self.player and self.board[x, y+3] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.column-y <= 4:
            if self.board[x, y-1] == self.player and self.board[x, y-2] == self.player and self.board[x, y-3] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.column-y >= 3 and y != 0:
            if self.board[x, y+1] == self.player and self.board[x, y+2] == self.player and self.board[x, y-1] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.column-y <= 5 and y != self.column-1:
            if self.board[x, y-1] == self.player and self.board[x, y-2] == self.player and self.board[x, y+1] == self.player:
                print("player ", self.player ," win")
                self.win = True

        #On regarde si le joueur gagne en diagonale
        if self.line-x >= 4 and self.column-y >= 4:
            if self.board[x+1, y+1] == self.player and self.board[x+2, y+2] == self.player and self.board[x+3, y+3] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x >= 3 and self.column-y >= 3 and x != 0 and y != 0:
            if self.board[x+1, y+1] == self.player and self.board[x+2, y+2] == self.player and self.board[x-1, y-1] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x >= 4 and self.column-y <= 4:
            if self.board[x+1, y-1] == self.player and self.board[x+2, y-2] == self.player and self.board[x+3, y-3] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x >= 3 and self.column-y <= 5 and x != 0 and y != self.column-1:
            if self.board[x+1, y-1] == self.player and self.board[x+2, y-2] == self.player and self.board[x-1, y+1] == self.player:
                print("player ", self.player ," win")
                self.win = True

        # On regarde si le joueur gagne en diagonale
        if self.line-x <= 3 and self.column-y >= 4:
            if self.board[x-1, y+1] == self.player and self.board[x-2, y+2] == self.player and self.board[x-3, y+3] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x <= 4 and self.column-y >= 3 and x != self.line-1 and y != 0:
            if self.board[x-1, y+1] == self.player and self.board[x-2, y+2] == self.player and self.board[x+1, y-1] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x <= 3 and self.column-y <= 4:
            if self.board[x-1, y-1] == self.player and self.board[x-2, y-2] == self.player and self.board[x-3, y-3] == self.player:
                print("player ", self.player ," win")
                self.win = True

        if self.line-x <= 4 and self.column-y <= 5 and x != self.line - 1 and y != self.column - 1:
            if self.board[x-1, y-1] == self.player and self.board[x-2, y-2] == self.player and self.board[x+1, y+1] == self.player:
                print("player ", self.player ," win")
                self.win = True


    def convert_coordinates(self, i, j):  # Converti les coordonnées dans le tableau en coordonnée sur la fenêtre
        return self.height - (i * self.height / self.line), j * self.width / self.column


    def print_board(self):

        #Création de la grille
        self.geometry("700x600")
        for i in range(6):  # nombre de lignes
            self.canvas.create_line(100 * (i + 1), 0, 100 * (i + 1), self.height, width=5)
        for i in range(7):  # nombre de colonnes
            self.canvas.create_line(0, 100 * (i + 1), self.width, 100 * (i + 1), width=5)
        self.canvas.pack()

        #Ajoute les jetons dans la grille
        for i in range (self.line) :
            for j in range (self.column) :
                if (self.board[i,j]==1) :
                    x0, y0 = self.convert_coordinates(i, j + 1)
                    x1, y1 = self.convert_coordinates(i + 1, j)
                    self.canvas.create_oval(y0, self.height - x0, y1, self.height - x1, outline="gray", fill="red",
                                            width=2, tag="J1")
                elif (self.board[i,j]==2) :
                    x0, y0 = self.convert_coordinates(i, j + 1)
                    x1, y1 = self.convert_coordinates(i + 1, j)
                    self.canvas.create_oval(y0, self.height - x0, y1, self.height - x1, outline="gray", fill="yellow",
                                            width=2, tag="J2")
        #self.frame.update()
        self.canvas.update()







