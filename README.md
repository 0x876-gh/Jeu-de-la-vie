# Jeu-de-la-vie
'Game Of Life' de Conway fait en cours.


## Principe

Le **Jeu de la vie** est un automate cellulaire imaginé par le mathématicien **John Conway** en 1970. Les cellules peuvent être **vivante** ou **morte**. L'état des cellules évolue en fonction de ces 3 règles simples :

- Une cellule vivante **meurt** si elle a moins de 2 ou plus de 3 voisines vivantes.
- Une cellule vivante **survit** si elle a 2 ou 3 voisines vivantes.
- Une cellule **prend vie** si elle a 3 voisines vivantes.

Avec ces règles, on peut créer des structures stables comme par exemple le **bloc**, qui est constitué de 4 cellules formant un carré.
Dans mon programme, j'ai représenté la grille par une matrice de listes Python imbriquées qui contiennent des entiers 0 ou 1, 1 pour **vivant** et 0 pour **mort**.

## Installation

Pour lancer ce programme sur votre ordinateur il faut Python 3.7 et le module matplotlib, voici la commande pour lancer le programme:

**macOS / Linux :**

```python3 game_of_life.py```

**Windows :**

```python game_of_life.py```
