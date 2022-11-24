#Les imports

import copy
from sklearn.neural_network import MLPClassifier
import numpy as np
import random
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree


class Morpion:

    def __init__(self):
        self.plateau = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.J1 = 'X'
        self.J2 = 'O'

        #base d'observations
        self.base_de_jeu = []
        #base de résultats
        self.base_resultat_jeu = []
        #création d'un classifieur
        #réseau de neurones
        self.clf=MLPClassifier(solver='lbfgs',alpha = 1e-5, hidden_layer_sizes = (6,2),random_state = 1)
        #arbre de décision
        #self.clf=tree.DecisionTreeClassifier()


    def initialiser_plateau(self) :
        self.plateau = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

#def ai_jeu(self,i):

# def convert_plateau(self,plateau):


    def train_ai_jeu(self):

        #CHOIX : l'ia va jouer 10 fois 100 parties pour apprendre
        nb_parties = 100
        for i in range(0,10):
            victoire_j1=0
            victoire_ia=0
            egalite = 0

            #Stocker le résultat de la partie
            for j in range (0,nb_parties) :
                #ia joue une partie
                sauvegarde_plateaux, result=self.ai_jeu(i)
                if (result == self.J1):
                    victoire_j1+=1
                elif (result == self.J2) :
                    victoire_ia+=1
                else :
                    egalite+=1

                #sauvegarde de la partie jouée
                for k in range (0,len(sauvegarde_plateaux)) :
                    sauvegarde_plateaux[k] = np.array(sauvegarde_plateaux[k]).reshape(-1)
                    sauvegarde_plateaux[k] = self.convert_plateau(sauvegarde_plateaux[k])
                    sauvegarde_plateaux[k] = sauvegarde_plateaux[k].astype(np.float64)

                    self.base_de_jeu.append(sauvegarde_plateaux[k])
                    #Si j1 a gagné
                    if (result == self.J1) :
                        self.base_resultat_jeu.append(0)
                    elif (result == self.J2) :
                        self.base_resultat_jeu.append(1)

            #Affichage des résultats après nb_parties
            print ("Itération = ",i ,  " victoire J1 = ", victoire_j1,  "victoire IA = ", victoire_ia,  "egalite = ", egalite)

            #Actualiser l'intelligence de l'ia
            self.train_ai_player()

    def jeu(self) :
        morpion.afficher_plateau()
        bool_fin_jeu = False

        #Tant que le jeu n'est pas fini
        while bool_fin_jeu == False :

            #Joueur 1 joue
            morpion.jouer(slef.J1)
            morpion.affiher_plateau()
            #test victoire J1
            resultat_test_fin_jeu=self.test_fin_jeu(self.J1)
            if (resultat_test_fin_jeu==self.J1):
                print("Joueur " + self.J1 +" a gagné" )
                return self.J1
            #test fin de jeu égalité
            elif (resultat_test_fin_jeu==True):
                print("Égalité entre les joueurs")
                return "égalité"

            # même chose avec le joueur 2
            morpion.jouer(slef.J2)
            morpion.affiher_plateau()
            resultat_test_fin_jeu = self.test_fin_jeu(self.J2)
            if (resultat_test_fin_jeu == self.J2):
                print("Joueur " + self.J2 + " a gagné")
                return self.J2
            # test fin de jeu égalité
            elif (resultat_test_fin_jeu == True):
                print("Égalité entre les joueurs")
                return "égalité"


    def generateur_de_mouvement(self, joueur):
        liste_mouvement_possible=[]
        for i in range (0,3) :
            for j in range (0,3) :
                #si la case courante est vide
                if (self.plateau[i][j] == "-") :
                    #création d'un mouvement virtuel et ajout de celui-ci à la liste des mouvement
                    virtual_plateau = copy.deepcopy(self.plateau)
                    virtual_plateau[i][j] = joueur
                    liste_mouvement_possible.append(virtual_plateau)
        return liste_mouvement_possible

    def train_ai_player(self) :
        self.scaler = preprocessing.StandardScaler().fit(self.base_de_jeu)
        X_train = self.scaler.transform(self.base_de_jeu)
        #entrainement du classifieur
        self.clf.fit(X_train, self.base_resultat_jeu)

    def entraineur_ai_joue(self, liste_mvt_possible) :
        if (len(liste_mvt_possible)>1):
            #un mouvement aléatoire est joué parmi ceux de la liste
            indice_mvt = random.randint(0, len(liste_mvt_possible) - 1)
            self.plateau = liste_mvt_possible[indice_mvt]
        else :
            self.plateau = liste_mvt_possible[0]


    def ai_player_joue(self, joueur, liste_mvt_possible) :
        liste_mvt_possible_copy = copy.deepcopy(liste_mvt_possible)
        for i in range (0,len(liste_mvt_possible_copy)) :
            liste_mvt_possible_copy[i] = self.convert_plateau(np.array(liste_mvt_possible_copy[i]).reshape(-1)).astype(np.float64)
        X_test = self.scaler.transform(liste_mvt_possible_copy)
        #ia calcul la probabilité de gagner selon chacun des mouvements possibles
        proba_success_mvt = self.clf.predict_proba(X_test)
        indice_mvt = 0
        #choix de la probabilité la plus grande
        for  i  in  range (0,  len(proba_success_mvt)):
            if (proba_success_mvt[indice_mvt][1] < proba_success_mvt[i][1]):
                indice_mvt = i
        self.plateau=liste_mvt_possible[indice_mvt]


    def afficher_plateau(self) :
        for i in range(0,3) : # 0 1 2
            for j in range(0,3) :
                print("|", end="")
                print(self.plateau[i][j], end="")
            print ("|")
        print("-----------------------------------------")

    def test_fin_jeu(self, joueur) :

        #vérification sur chaque ligne
        for i in range (0,3) :
            compteur = 0
            for j in range (0,3) :
                if self.plateau[i][j]==joueur :
                    compteur+=1
            if compteur == 3 :
                return joueur #joueur vainqueur

        #vérification sur chaque colonne
        for i in range(0, 3):
            compteur = 0
            for j in range(0, 3):
                if self.plateau[j][i] == joueur:
                    compteur += 1
            if compteur == 3:
                return joueur

        #vérification diagonale 1
        compteur = 0
        for i in range (0,3) :
            if self.plateau[i][i] == joueur :
                compteur+=1
        if compteur == 3 :
            return joueur

        #vérification diagonale 2
        compteur = 0
        for i in range (0,3) :
            if self.plateau[2-i][i] == joueur :
                compteur+=1
        if compteur == 3 :
            return joueur

        #vérification que le plateau n'est pas plein
        compteur = 0
        for i in range (0,3) :
            for j in range (0,3) :
                if (self.plateau[i][j] != '-') :
                    compteur += 1
        if compteur == 9 :
            return True
        else :
            return False


    def jouer(self, joueur) :
        x = input("Entrez l'abscisse compris entre 1 et 3")
        y = input("Entrez l'ordonnée entre 1 et 3")
        self.plateau[int(x)][int(y)] = joueur






