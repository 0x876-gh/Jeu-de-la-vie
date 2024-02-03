# Créé par lepinv, le 18/01/2024 en Python 3.7

import random
import matplotlib.pyplot as plt

largeur = 20
hauteur = 20

MatriceN = [[random.choice([0,1]) for i in range(largeur)] for i in range(hauteur)]

Matrice = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

verif = [[0 for i in range(largeur)] for i in range(hauteur)]


def voisins(x, y, matr):
    n = 0
    plus = 1
    moins = 1
    try:
        test = matr[x+1][y+1]
    except:
        plus = 0

    try:
        test = matr[x-1][y-1]
    except:
        moins = 0

    if matr[x+plus][y] == 1:
        n += 1
    if matr[x+plus][y+plus] == 1:
        n += 1
    if matr[x][y+plus] == 1:
        n += 1
    if matr[x-moins][y+plus] == 1:
        n += 1
    if matr[x-moins][y] == 1:
        n += 1
    if matr[x-moins][y-moins] == 1:
        n += 1
    if matr[x][y-moins] == 1:
        n += 1
    if matr[x+plus][y-moins] == 1:
        n += 1

    return n


while True:
    for x in range(len(Matrice)):
        for y in range(len(Matrice[0])):
            etat = Matrice[x][y]
            if etat == 0:
                if voisins(x, y, Matrice) == 3:
                    verif[x][y] = 1
            if etat == 1:
                if voisins(x, y, Matrice) == 0 or voisins(x, y, Matrice) == 1 or voisins(x, y, Matrice) == 4 or voisins(x, y, Matrice) == 5 or voisins(x, y, Matrice) == 6 or voisins(x, y, Matrice) == 7 or voisins(x, y, Matrice) == 8:
                    verif[x][y] = 0
                else:
                    verif[x][y] = 1

    Matrice = verif
    verif = [[0 for i in range(largeur)] for i in range(hauteur)]

    plt.imshow(Matrice)
    plt.pause(0.01)
    plt.clf()
