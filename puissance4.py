# -*- coding: utf-8 -*-
"""
Created on :
@author:
"""

from tkinter import *
import numpy as np
import time



class Puissance4(Tk):



    def callback(self, event):
        print ("Clic")
        #self.frame.focus_set()
        x = event.x
        x = int(x * self.height / self.width)
        self.play(x, 1, True)
        ARTIF = IA.P4IA(self, 2)
        ARTIF.coup_IA(8)

    def __init__(self):
        Tk.__init__(self)
        self.column = 7
        self.line = 6
        self.width = 700
        self.height = 600
        self.player = 1
        self.reset()
        #Permet de resize les éléments quand on change la taille de la fenêtre
        #self.frame.pack()
        self.canvas.pack()

    def reset(self):
        self.board = np.zeros((self.line, self.column))
        #self.frame = Frame(self, width=self.width, height=self.height)
        self.canvas = Canvas(self, width=self.width, height=self.height, background='blue')

    def possibles_plays(self):
        plays = []
        for i in range(self.column):
            for j in range(self.line):
                if self.board[self.line-j-1,i] == 0:
                    plays.append([self.line-j-1,i])
                    break

        return plays

    def play(self, position):

        if position not in self.possibles_plays():
            print("Ce coup n'est pas possible, rejouez !")
        else:
            self.board[position] = self.player

            self.check_win(position, self.player)

            if self.player == 1:
                self.player = 2
            else:
                self.player = 1




    def check_win(self, position, player):
        x = position[0]
        y = position[1]

        if np.sum(self.board) == 63:
            raise IndexError("Egalite")
        return False

        # On regarde si le joueur gagne en colonne
        if self.line-x >= 4:
            if self.board[x+1,y] == player & self.board[x+2,y] == player & self.board[x+3,y] == player:
                print("player "+player+" win")
                return True

        if self.line-x <= 3:
            if self.board[x-1,y] == player & self.board[x-2,y] == player & self.board[x-3,y] == player:
                print("player "+player+" win")
                return True

        if self.line - x >= 3 & x != 0:
            if self.board[x+1,y] == player & self.board[x+2,y] == player & self.board[x-1,y] == player:
                print("player " + player + " win")
                return True

        if self.line - x <= 4 & x != self.line-1:
            if self.board[x-1,y] == player & self.board[x-2,y] == player & self.board[x+1,y] == player:
                print("player " + player + " win")
                return True

        #On regarde si le joueur gagne en ligne
        if self.column-y >= 4:
            if self.board[x,y+1] == player & self.board[x,y+2] == player & self.board[x,y+3] == player:
                print("player "+player+" win")
                return True

        if self.column-y <= 4:
            if self.board[x,y-1] == player & self.board[x,y-2] == player & self.board[x,y-3] == player:
                print("player "+player+" win")
                return True

        if self.column-y >= 3 & y != 0:
            if self.board[x,y+1] == player & self.board[x,y+2] == player & self.board[x,y-1] == player:
                print("player "+player+" win")
                return True

        if self.column-y <= 5 & y != self.column-1:
            if self.board[x,y-1] == player & self.board[x,y-2] == player & self.board[x,y+1] == player:
                print("player "+player+" win")
                return True

        #On regarde si le joueur gagne en diagonale
        if self.line-x >= 4 & self.column-y >= 4:
            if self.board[x+1,y+1] == player & self.board[x+2,y+2] == player & self.board[x+3,y+3] == player:
                print("player "+player+" win")
                return True

        if self.line-x >= 3 & self.column-y >= 3 & x != 0 & y != 0:
            if self.board[x+1, y+1] == player & self.board[x+2, y+2] == player & self.board[x-1,y-1] == player:
                print("player "+player+" win")
                return True

        if self.line-x >= 4 & self.column-y <= 4:
            if self.board[x+1,y-1] == player & self.board[x+2,y-2] == player & self.board[x+3,y-3] == player:
                print("player " + player + " win")
                return True

        if self.line-x >= 3 & self.column-y <= 5 & x != 0 & y != self.column-1:
            if self.board[x+1,y-1] == player & self.board[x+2,y-2] == player & self.board[x-1,y+1] == player:
                print("player " + player + " win")
                return True

        # On regarde si le joueur gagne en diagonale
        if self.line-x <= 3 & self.column-y >= 4:
            if self.board[x-1,y+1] == player & self.board[x-2,y+2] == player & self.board[x-3,y+3] == player:
                print("player " + player + " win")
                return True

        if self.line-x <= 4 & self.column-y >= 3 & x != self.line-1 & y != 0:
            if self.board[x-1,y+1] == player & self.board[x-2,y+2] == player & self.board[x+1,y-1] == player:
                print("player " + player + " win")
                return True

        if self.line-x <= 3 & self.column-y <= 4:
            if self.board[x-1,y-1] == player & self.board[x-2,y-2] == player & self.board[x-3,y-3] == player:
                print("player " + player + " win")
                return True

        if self.line-x <= 4 & self.column-y <= 5 & x != self.line - 1 & y != self.column - 1:
            if self.board[x-1,y-1] == player & self.board[x-2,y-2] == player & self.board[x+1,y+1] == player:
                print("player " + player + " win")
                return True

        return False

    def convert_coordinates(self, i, j):  # Converti les coordonnées dans le tableau en coordonnée sur la fenêtre
        return self.height - (
                self.line - i) * self.height / self.column, j * self.L / self.width

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








