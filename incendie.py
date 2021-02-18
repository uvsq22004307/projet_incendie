###################################################
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# https://github.com/uvsq22004307/projet_incendie
###################################################


# Import des librairies

import tkinter as tk
from random import random

import numpy as np


# Définition des constantes (écrites en majuscule)


# Définition des variables globales


# Définition des fonctions (chaque fonction devra contenir une docstring)


def hasard(p):
    """Renvoie True avec une probabilité p et False avec une probabilité 1-p"""
    assert 0 <= p <= 1  # verifions que p est dans [0,1]

    r = random()  # On prend au hasard un nombre entre 0 et 1
    return r <= p  # Si r<=p (une proba p) on retourne True sinon on retourne False (une proba 1-p)


def creerForet(x, y, pcocup):
    """Cree une foret avec des arbres et de l'eau placés aleatoirements"""
    foret = np.zeros((x, y))  # on cree un matrice x*y de zeros
    for i in range(x):
        for j in range(y):
            if hasard(pcocup):
                foret[i, j] = 1.  # Si on une proba p alors il y a un arbre
            else:
                foret[i, j] = 0.  # Sinon il n'y a pas d'arbre mais de l'eau
    return foret


def mettre_le_feu(foret, i, j):
    """Met le feu a un arbre"""
    if foret[i, j] == 1:
        foret[i, j] = 2.  # On met le feu la case d'indice  (i,j)
    return foret


def draw_grid(canvas, grid, height, width):
    """Dessine la grille dans le canvas."""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            x = width / len(row)
            y = height / len(grid)

            canvas.create_rectangle(j * x, i * y, j * x + x, i * y + y, fill=color(cell), tag=str(i)+":"+str(j), outline="")


def change_element_on_grid(canvas, i, j, element):
    """Change la couleur d'un élément dans le canvas."""
    canvas.itemconfigure(str(i)+":"+str(j), fill=color(element))


def color(element):
    """Renvoie la couleur de l'élément correspondant."""
    switcher = {
        0: "blue",  # Eau
        1: "green",  # Forêt
        2: "red",  # Feu
        3: "yellow",  # Prairie
        4: "gray",  # Cendres tièdes
        5: "black"  # Cendres éteintes
    }
    return switcher.get(element, "blue")


# Programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boule de gestion des événements
root = tk.Tk()
root.title("Projet Incendie")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

foret = tk.Button(root, text="crée une foret", command=creerForet())
foret.pack()
feu = tk.Button(root, text="crée une foret", command=mettre_le_feu())
feu.pack()

root.mainloop()
