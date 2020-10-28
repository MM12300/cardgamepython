import random

class jeuDeCarte : 
    def __init__(self):
        self.paquet = []
        self.valeurs = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.signes = [ "Coeur", "Carreau", "Pique", "Trefle" ]
        

        for signe in self.signes:
            for valeur in self.valeurs:
                if valeur == 11 :
                    carte = "Valet de " + signe
                elif valeur == 12 : 
                    carte = "Reine de " + signe
                elif valeur == 13 : 
                    carte = "Roi de " + signe
                elif valeur == 1 : 
                    carte = "As de " + signe
                else : 
                    carte = str(valeur) + " de " + signe
                self.paquet.append((valeur, signe, carte))

    def melangePaquet(self,paquet):
            random.shuffle(paquet)

class partie : 
    def __init__(self, jeuDeCarte, joueur1, joueur2) : 
        self.jeuDeCarte = jeuDeCarte
        self.joueur1 = joueur()
        self.joueur2 = joueur()


    def distribuer(self, jeuDeCarte, joueur1, joueur2):
        print(self.jeuDeCarte.paquet)
        self.jeuDeCarte.melangePaquet(self.jeuDeCarte.paquet)
        for n in range(len(self.jeuDeCarte.paquet)):
            if n % 2 == 0 : 
                self.joueur1.mainDuJoueur.append(self.jeuDeCarte.paquet.pop())
            else:
                self.joueur2.mainDuJoueur.append(self.jeuDeCarte.paquet.pop())

        print("main du joueur 1")
        print(len(self.joueur1.mainDuJoueur))
        print(self.joueur1.mainDuJoueur)
        print("main du joueur 2")
        print(len(self.joueur2.mainDuJoueur))
        print(self.joueur2.mainDuJoueur)
        print("paquet")
        print(self.jeuDeCarte.paquet)



        

class joueur : 
    def __init__(self):
        self.mainDuJoueur=[]


def main():
    jeu = jeuDeCarte()
    print(jeu.paquet)
    # print(jeu.paquet)
    jeu.melangePaquet(jeu.paquet)
    #print(jeu.paquet)
    partieEnCours = partie(jeuDeCarte(), joueur(), joueur())
    #print(partieEnCours.jeuDeCarte.paquet)

    
    #AFFICHAGE CARTE DISTRIBUEE
    #partieEnCours.distribuer(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2)
   
   
   
    #print(partieEnCours.jeuDeCarte.paquet)

    #joueur1 = joueur()
    #joueur1.mainDuJoueur

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