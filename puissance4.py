# -*- coding: utf-8 -*-
"""
Created on :
@author:
"""

from tkinter import *
import numpy as np
import math
import random
import matplotlib.pyplot as plt

class Puissance4(Tk):

    def callback(self, event):
        x = event.x
        x = int(x * self.column / self.width)
        self.play(x)

        if self.check_win(self.board) != -1:
            self.restart()
        else:
            x = self.minmax(self.board,5,-math.inf,math.inf,True)[0]
            self.play(x)

            if self.check_win(self.board) != -1:
                self.restart()

    def IA_vs_rand(self):
        if self.player == 1:
            x = self.minmax(self.board, 5, -math.inf, math.inf, True)[0]
            self.play(x)

        if self.check_win(self.board) != -1:
            self.restart()
            self.loose += 1
            print("Win: ", self.win, ", Loose: ", self.loose)
            self.tab.append(-1)
        else:
            if self.player == 2:
                x = self.minmax(self.board, 5, -math.inf, math.inf, True)[0]
                self.play(x)

                if self.check_win(self.board) != -1:
                    self.restart()
                    self.win += 1
                    print("Win: " , self.win , ", Loose: " , self.loose)
                    self.tab.append(1)

        if len(self.tab) == 100:
            t = np.linspace(0, 100, 100)
            plt.plot(t,self.tab)
            plt.show()
        else:
            self.IA_vs_rand()

    def motion(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))

    def __init__(self):
        Tk.__init__(self)
        self.tab = []
        self.win = 0
        self.loose = 0
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
        self.player = 1
        self.board = np.zeros((self.line, self.column))
        self.canvas.delete("all")
        self.print_board()

    def possibles_plays(self, board):
        plays = []
        for i in range(self.column):
            for j in range(self.line):
                if board[self.line-j-1,i] == 0:
                    plays.append(self.line-j-1)
                    break
                elif j == self.line-1:
                    plays.append(-1)

        return plays

    def play(self, x):
        if self.possibles_plays(self.board)[x] == -1:
            print("Ce coup n'est pas possible, rejouez !")
        else:
            self.board[self.possibles_plays(self.board)[x], x] = self.player

            self.check_win(self.board)

            self.print_board()

            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

    def check_win(self, board):

        # Check horizontal locations for win
        for i in range(self.column - 3):
            for j in range(self.line):
                piece = board[j][i]
                if  board[j][i + 1] == piece and board[j][i + 2] == piece and board[j][i + 3] == piece and piece != 0:
                    return piece

        # Check vertical locations for win
        for i in range(self.column):
            for j in range(self.line - 3):
                piece = board[j][i]
                if board[j + 1][i] == piece and board[j + 2][i] == piece and board[j + 3][i] == piece and piece != 0:
                    return piece

        # Check positively sloped diaganols
        for i in range(self.column - 3):
            for j in range(self.line - 3):
                piece = board[j][i]
                if board[j + 1][i + 1] == piece and board[j + 2][i + 2] == piece and board[j + 3][i + 3] == piece and piece != 0:
                    return piece

        # Check negatively sloped diaganols
        for i in range(self.column - 3):
            for j in range(3, self.line):
                piece = board[j][i]
                if board[j - 1][i + 1] == piece and board[j - 2][i + 2] == piece and board[j - 3][i + 3] == piece and piece != 0:
                    return piece

        return -1

    def convert_coordinates(self, i, j):  # Converti les coordonnées dans le tableau en coordonnée sur la fenêtre
        return self.height - (i * self.height / self.line), j * self.width / self.column

    def print_board(self):

        #Ajoute les jetons dans la grille
        for i in range (self.line):
            for j in range (self.column):
                if self.board[i, j] == 0:
                    x0, y0 = self.convert_coordinates(i, j + 1)
                    x1, y1 = self.convert_coordinates(i + 1, j)
                    self.canvas.create_oval(y0 - 5, self.height - x0 + 5, y1 + 5, self.height - x1 - 5, outline="gray", fill="white",
                                            width=2, tag="J1")
                elif self.board[i, j] == 1:
                    x0, y0 = self.convert_coordinates(i, j + 1)
                    x1, y1 = self.convert_coordinates(i + 1, j)
                    self.canvas.create_oval(y0 - 5, self.height - x0 + 5, y1 + 5, self.height - x1 - 5, outline="gray", fill="red",
                                            width=2, tag="J1")
                elif self.board[i, j] == 2:
                    x0, y0 = self.convert_coordinates(i, j + 1)
                    x1, y1 = self.convert_coordinates(i + 1, j)
                    self.canvas.create_oval(y0 - 5, self.height - x0 + 5, y1 + 5, self.height - x1 - 5, outline="gray", fill="yellow",
                                            width=2, tag="J2")
        #self.frame.update()
        self.canvas.update()

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def minmax(self, board, depth, alpha, beta, flag_max):
        possible_play = self.possibles_plays(board)

        valid_col = []
        for i in range(len(possible_play)):
            if possible_play[i] != -1:
                valid_col.append(i)

        win = self.check_win(board)

        if depth == 0 or win != -1:
            if win == 2:
                return (None, 100000000000000)
            elif win == 1:
                return (None, -10000000000000)
            elif win == 0:
                return (None, -1)
            else:
                return (None, 0)

        if flag_max:
            value = -math.inf
            column = random.choice(valid_col)

            for col in valid_col:
                row = possible_play[col]
                b_copy = self.board.copy()

                self.drop_piece(b_copy, row, col, 2)
                new_score = self.minmax(b_copy, depth-1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

            return column, value

        else:
            value = math.inf
            column = random.choice(valid_col)

            for col in valid_col:
                row = possible_play[col]
                b_copy = self.board.copy()
                self.drop_piece(b_copy, row, col, 1)
                new_score = self.minmax(b_copy, depth-1,alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    column = col

                beta = min(beta, value)

                if alpha >= beta:
                    break

            return column, value







