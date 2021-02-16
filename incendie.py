###################################################
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# https://github.com/uvsq22004307/projet_incendie
###################################################



#import des librairies

import tkinter as tk
root = tk.Tk()
root.title("Projet Incendie")
from random import random
import numpy as np
canvas = tk.Canvas( width = 500, height = 500)


#définition des constantes (écrites en majuscule)




#définition des variables globales




#définition des fonctions (chaque fonction devra contenir une docstring)


def hasard(p):
   "renvoie True avec une probabilité p et False avec une probabilité 1-p"
   r=random() # on prend au hasard un nombre entre 0 et 1
   assert p>=0 and p<=1  # verifions que p est dans [0,1]
   return r <= p # si r<=p (une proba p) on retourne True sinon on retourne False (une proba 1-p)
             

def creerForet(x,y,pcocup):
    "cree une foret avec des arbres et de l'eau placés aleatoirements"
    foret=np.zeros((x,y)) # on cree un matrice x*y de zeros
    for i in range(x):
        for j in range(y):
            if hasard(pcocup):
                foret[i,j]=1. # si on une proba p alors il y a un arbre
            else:
                foret[i,j]=0. # sinon il n'y a pas d'arbre mais de l'eau
    return foret

def mettre_le_feu(foret,i,j):
    "met le feu a un arbre"
    if foret[i,j]==1:
        foret[i,j]=2. # on met le feu la case d'indice (i,j)
    return foret



#programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boule de gestion des événements

foret = tk.Button(root, text="crée une foret", command= creerForet() )
foret.pack()
feu = tk.Button(root, text="crée une foret", command= mettre_le_feu() )
feu.pack()




root.mainloop()