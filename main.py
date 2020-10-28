import random

class jeuDeCarte : 
    def __init__(self):
        self.paquet = []
        self.valeurs = [ 1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.signes = [ "Coeur", "Carreau", "Pique", "Trefle" ]

        for signe in self.signes:
            for valeur in self.valeurs:
                self.paquet.append((valeur, signe))

    def melangePaquet(self,paquet):
            random.shuffle(paquet)

class partie : 
    def __init__(self, jeuDeCarte, joueur1, joueur2) : 
        self.jeuDeCarte = jeuDeCarte
        self.joueur1 = joueur
        self.joueur2 = joueur


    def distribuer(self, jeuDeCarte, joueur1, joueur2):
        print(self.jeuDeCarte.paquet)
        self.jeuDeCarte.melangePaquet(self.jeuDeCarte.paquet)
        


        

class joueur : 
    def __init__(self):
        self.mainDuJoueur=[]


def main():
    jeu = jeuDeCarte()
    # print(jeu.paquet)
    jeu.melangePaquet(jeu.paquet)
    #print(jeu.paquet)
    partieEnCours = partie(jeuDeCarte(), joueur(), joueur())
    #print(partieEnCours.jeuDeCarte.paquet)

    partieEnCours.distribuer(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2)
    print(partieEnCours.jeuDeCarte.paquet)

    # liste = [1,2,3,4,5]
    # print(liste)
    # liste2 = []
    # print(liste)
    # for n in range(2):
    #    liste2.append(liste.pop())
    # print(liste)
    # print(liste2)




if __name__=='__main__':
    main()