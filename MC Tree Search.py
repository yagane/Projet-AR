import random
import math
import copy
import time
from puissance4 import *


class Node():

    # State est une matrice de notre jeu actuel
    # définition d'un noeud + par défaut, root car pas de parent
    def __init__(self, state, parent=None):
        self.visits = 1
        self.reward = 0.0
        #valeur utc
        self.valeur = 0
        # matrice du plateau board
        self.state = state
        # liste des noeuds enfants
        self.children = []
        #entier correspondant à la colonne jouée
        self.move = 1
        self.parent = parent

    # enfant d'un noeud
    def addChild(self, P4):
        coups = P4.possibles_plays(self.state)
        for i in range (len(coups)) :
            if coups[i]>-1 :
                copy_board = P4.board
                P4.drop_piece(copy_board, P4.possibles_plays(copy_board)[self.move], self.move, P4.player)
                child_state = copy_board
                child = Node(child_state, self)
                self.children.append(child)
        return


    # le noeud a-t-il était était completement exploré
    def fully_explored(self):
        if len(self.children) == 0 and self.visits>0:
            return True
        bool = True
        for i in range (len(self.children)) :
            if not self.children[i].fully_explored() :
                bool = False
                break
        return bool


# root est un node sans parent
def monte_carlo_tree_search(root, profondeur, P4):
    time_debut = time.time()
    Node = root

    #Création de l'arbre
    creation_arbre(root, P4)


    while (time.time() - time_debut < duree_max):
        Node = traverse(Node)
        rollout(Node, P4)
        retropropagation(Node, P4)

    return best_child(Node).move


def creation_arbre(root, P4): #4étages
    root.addChild(P4)
    for i in range (len(root.children)) :
        root.children[i].addChild()
        for j in range (len(root.children[i])) :
            root.children[i].children[j].addChild(P4)
    return


# sélection et expansion
def traverse(node):
    while node.fully_explored():
        node = best_uct(node)
    return node  # ou noeud non visité ?


# simulation + s'arrête quand victoire
def rollout(node, P4):
    copy_board = P4.board
    while P4.check_win(copy_board) == -1:
        node = rollout_policy(node)
        if node.move in P4.possibles_plays(copy_board) :
            P4.drop_piece(copy_board, P4.possibles_plays(copy_board)[node.move], node.move, P4.player)
            node.state = copy_board
    return node.state


# politique de choix : choix d'un noeud au hasard parmi les enfant
def rollout_policy(node):
    if (len(node.children) > 0):
        a = np.randint(1, len(node.children))
        return node.children[a - 1]
    return node


# retropropagation
def retropropagation(Node, P4):
    if Node.parent == None:
        return
    Node.visits += 1
    Node.reward += P4.score_board(Node.state, P4.player)
    retropropagation(Node.parent, P4)


# choix de l'enfant avec le plus de visite
def best_child(Node):
    if (len(Node.children) > 0):
        max_visit = 0
        node = Node
        for i in Node.children:
            if i.visits > max_visit:
                max_visit = i.visits
                node = i
        return node
    return Node


# Méthode de séléction avec la plus grande valeur des noeuds
def best_uct(Node):
    if (len(Node.children) > 0):
        for i in Node.children:
            i.valeur = i.reward / i.visits + 1.2 * np.sqrt(i.visits)

        max_val = 0
        node = Node
        for i in Node.children:
            if (i.valeur > max_val):
                max_val = i.valeur
                node = i
        return node
    return Node
