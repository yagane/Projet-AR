# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:30:17 2016
@author: Maxime
"""

import numpy as np
import random as rd
from tkinter import *
import P4_IA as IA


def convert_coordinates(i, j):  # Converti les coordonnées dans le tableau en coordonnée sur la fenêtre
    return Puissance4.H - (
                Puissance4.hauteur - i) * Puissance4.H / Puissance4.hauteur, j * Puissance4.L / Puissance4.longueur


class Puissance4(Tk):
    column = 7.
    line = 6.
    width = 300
    height = (line/column) * W
    player = 1


    def callback(self, event):
        print "Clic"
        self.frame.focus_set()
        x = event.x
        x = int(x * Puissance4.width / Puissance4.W)
        self.play(x, 1, True)
        ARTIF = IA.P4IA(self, 2)
        ARTIF.coup_IA(8)

    def __init__(self):
        Tk.__init__(self)
        self.board = np.zeros(Puissance4.line, Puissance4.column)
        self.frame = Frame(self, width=Puissance4.width, height=Puissance4.height)
        self.canvas = Canvas(self, width=Puissance4.width, height=Puissance4.height)

    def reset(self):
        self.board = np.zeros(Puissance4.line, Puissance4.column)
        self.frame = Frame(self, width=Puissance4.width, height=Puissance4.height)
        self.canvas = Canvas(self, width=Puissance4.width, height=Puissance4.height)

    def possibles_plays(self):
        plays = []
        for i in range(Puissance4.column):
            for j in range(Puissance4.line):
                if self.board[Puissance4.line-j-1,i] == 0:
                    plays.append([Puissance4.line-j-1,i])
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
        if Puissance4.line-x >= 4:
            if self.board[x+1,y] == player & self.board[x+2,y] == player & self.board[x+3,y] == player:
                print("player "+player+" win")
                return True

        if Puissance4.line-x <= 3:
            if self.board[x-1,y] == player & self.board[x-2,y] == player & self.board[x-3,y] == player:
                print("player "+player+" win")
                return True

        if Puissance4.line - x >= 3 & x != 0:
            if self.board[x+1,y] == player & self.board[x+2,y] == player & self.board[x-1,y] == player:
                print("player " + player + " win")
                return True

        if Puissance4.line - x <= 4 & x != Puissance4.line-1:
            if self.board[x-1,y] == player & self.board[x-2,y] == player & self.board[x+1,y] == player:
                print("player " + player + " win")
                return True

        #On regarde si le joueur gagne en ligne
        if Puissance4.column-y >= 4:
            if self.board[x,y+1] == player & self.board[x,y+2] == player & self.board[x,y+3] == player:
                print("player "+player+" win")
                return True

        if Puissance4.column-y <= 4:
            if self.board[x,y-1] == player & self.board[x,y-2] == player & self.board[x,y-3] == player:
                print("player "+player+" win")
                return True

        if Puissance4.column-y >= 3 & y != 0:
            if self.board[x,y+1] == player & self.board[x,y+2] == player & self.board[x,y-1] == player:
                print("player "+player+" win")
                return True

        if Puissance4.column-y <= 5 & y != Puissance4.column-1:
            if self.board[x,y-1] == player & self.board[x,y-2] == player & self.board[x,y+1] == player:
                print("player "+player+" win")
                return True

        #On regarde si le joueur gagne en diagonale
        if Puissance4.line-x >= 4 & Puissance4.column-y >= 4:
            if self.board[x+1,y+1] == player & self.board[x+2,y+2] == player & self.board[x+3,y+3] == player:
                print("player "+player+" win")
                return True

        if Puissance4.line-x >= 3 & Puissance4.column-y >= 3 & x != 0 & y != 0:
            if self.board[x+1, y+1] == player & self.board[x+2, y+2] == player & self.board[x-1,y-1] == player:
                print("player "+player+" win")
                return True

        if Puissance4.line-x >= 4 & Puissance4.column-y <= 4:
            if self.board[x+1,y-1] == player & self.board[x+2,y-2] == player & self.board[x+3,y-3] == player:
                print("player " + player + " win")
                return True

        if Puissance4.line-x >= 3 & Puissance4.column-y <= 5 & x != 0 & y != Puissance4.column-1:
            if self.board[x+1,y-1] == player & self.board[x+2,y-2] == player & self.board[x-1,y+1] == player:
                print("player " + player + " win")
                return True

        # On regarde si le joueur gagne en diagonale
        if Puissance4.line-x <= 3 & Puissance4.column-y >= 4:
            if self.board[x-1,y+1] == player & self.board[x-2,y+2] == player & self.board[x-3,y+3] == player:
                print("player " + player + " win")
                return True

        if Puissance4.line-x <= 4 & Puissance4.column-y >= 3 & x != Puissance4.line-1 & y != 0:
            if self.board[x-1,y+1] == player & self.board[x-2,y+2] == player & self.board[x+1,y-1] == player:
                print("player " + player + " win")
                return True

        if Puissance4.line-x <= 3 & Puissance4.column-y <= 4:
            if self.board[x-1,y-1] == player & self.board[x-2,y-2] == player & self.board[x-3,y-3] == player:
                print("player " + player + " win")
                return True

        if Puissance4.line-x <= 4 & Puissance4.column-y <= 5 & x != Puissance4.line - 1 & y != Puissance4.column - 1:
            if self.board[x-1,y-1] == player & self.board[x-2,y-2] == player & self.board[x+1,y+1] == player:
                print("player " + player + " win")
                return True

        return False

    def print_board(self):







