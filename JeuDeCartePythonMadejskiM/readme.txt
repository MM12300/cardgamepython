Évaluation Python Objet - MADEJSKI Matthieu CDAN 2020-2021

Version Python : 3.8.6

La Bataille, version console en langage Python :

Ce programme réalise une partie de bataille fermée entre deux joueurs.

(règles classiques concernant l'égalité lors d'une manche, cf. https://fr.wikipedia.org/wiki/Bataille_(jeu))

Les règles : 
On distribue un jeu de cartes (52, pas de joker) aux joueurs, qui n'en prennent pas connaissance. À chaque tour, chaque joueur retourne la carte du haut de sa main (ou son tas). Celui qui a la carte de la plus haute valeur — selon la hiérarchie du bridge : as, roi, dame, valet, dix… jusqu'au deux — fait la levée, qu'il place sous son tas.
En cas d'égalité de valeurs — cas appelé bataille — les joueurs en ballotage disent « bataille ! », et commencent par placer une première carte face cachée puis une seconde carte face visible pour décider qui fera la levée. En cas de nouvelle égalité, la procédure est répétée. À la fin, le joueur gagnant remporte toutes les cartes, qu'il place sous son tas. La bataille est parfois l'occasion d'acquérir une grosse carte et c'est l'unique manière de gagner un as. Sans bataille et à moins qu'un joueur ne possède tous les as, il serait impossible de terminer une partie de bataille.
Lorsqu'un joueur a en sa possession toutes les cartes du jeu, la partie se termine et il est déclaré gagnant. 


Comment exécuter le script : 
-> Soyez sûr avoir installé les modules utilisés (random, time et sys)
-> Exécutez le script bataille.py
==> Ce script est composé de 3 modules (partie.py, joueur.py et jeuDeCarte.py)

Customisation : 
Il n'est pas possible de changer le nombre de joueurs.
Il n'est pas possible, en l'état, d'ajouter ou de supprimer des règles.
Il est uniquement possible de changer le "print rendering" en modifiant le délai entre deux manches. (bataille.py, ligne 14)
Le contenu du paquet ainsi que les mains des joueurs sont privés, tout le reste de la partie est public. 


