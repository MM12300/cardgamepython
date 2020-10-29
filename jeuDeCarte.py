import random

#Représente un paquet de carte français classique de 52 cartes
#De base le paquet est rangé par signe, de 2 à As pour chaque signe
#Méthodes :
# - melangepaquet : permet de mélanger le paquet avec random
class jeuDeCarte : 
    def __init__(self):
        self.paquet = []
        self.valeurs = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.signes = [ "Coeur", "Carreau", "Pique", "Trèfle" ]

        for signe in self.signes:
            for valeur in self.valeurs:
                if valeur == 11 :
                    carte = "Valet de " + signe
                elif valeur == 12 : 
                    carte = "Reine de " + signe
                elif valeur == 13 : 
                    carte = "Roi de " + signe
                elif valeur == 14 : 
                    carte = "As de " + signe
                else : 
                    carte = str(valeur) + " de " + signe
                self.paquet.append((valeur, signe, carte))

    def melangePaquet(self,paquet):
            random.shuffle(paquet)