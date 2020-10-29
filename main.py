import random
import time
import sys


class jeuDeCarte : 
    def __init__(self):
        self.paquet = []
        self.valeurs = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.signes = [ "Coeur", "Carreau", "Pique", "Trefle" ]

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

class partie : 
    def __init__(self, jeuDeCarte, joueur1, joueur2) : 
        self.jeuDeCarte = jeuDeCarte
        self.joueur1 = joueur()
        self.joueur2 = joueur()
        self.plateauDeJeu=[]

    def distribuer(self, jeuDeCarte, joueur1, joueur2):
        #print(self.jeuDeCarte.paquet)
        self.jeuDeCarte.melangePaquet(self.jeuDeCarte.paquet)
        for n in range(len(self.jeuDeCarte.paquet)):
            if n % 2 == 0 : 
                self.joueur1.mainDuJoueur.append(self.jeuDeCarte.paquet.pop())
            else:
                self.joueur2.mainDuJoueur.append(self.jeuDeCarte.paquet.pop())



    def jouerUneManche(self, jeuDeCarte, joueur1, joueur2):
        print("MANCHE-------------------")
        print("Le joueur 1 a " + str(len(self.joueur1.mainDuJoueur)) + "cartes")
        print("---------------")
        print("Le joueur 2 a " + str(len(self.joueur2.mainDuJoueur)) + "cartes")

        
        print("---------------")
        self.plateauDeJeu = (self.joueur1.mainDuJoueur.pop(),self.joueur2.mainDuJoueur.pop())
        print("Joueur 1 joue : " + self.plateauDeJeu[0][2]+" contre " + "joueur 2 joue : " + self.plateauDeJeu[1][2]) 

        #règles du jeu
        totalCarteJoueur1 = len(self.joueur1.mainDuJoueur)
        totalCarteJoueur2= len(self.joueur2.mainDuJoueur)
        
        if totalCarteJoueur1 == 0 :
            #print("Le joueur 1 a perdu")
            self.joueur2.mainDuJoueur.append(self.plateauDeJeu[0])
            self.joueur2.mainDuJoueur.append(self.plateauDeJeu[1])
            sys.exit('le joueur 2 a gagné ! Bravo')
        elif totalCarteJoueur2 == 0 : 
            #print("le joueur 2 a perdu")
            self.joueur1.mainDuJoueur.append(self.plateauDeJeu[0])
            self.joueur1.mainDuJoueur.append(self.plateauDeJeu[1])
            sys.exit('le joueur 1 a gagné ! Bravo')

        else : 
            if self.plateauDeJeu[0][-1] == self.plateauDeJeu[1][-1] :
                self.plateauDeJeu = (self.joueur1.mainDuJoueur.pop(),self.joueur2.mainDuJoueur.pop())
                self.plateauDeJeu = (self.joueur1.mainDuJoueur.pop(),self.joueur2.mainDuJoueur.pop())
                
            else :
                if self.plateauDeJeu[0][-1] < self.plateauDeJeu[1][-1] :   
                    print("joueur 2 gagnant")
                    print("---------------")
                    self.joueur2.mainDuJoueur.append(self.plateauDeJeu[0])
                    self.joueur2.mainDuJoueur.append(self.plateauDeJeu[1])
                elif self.plateauDeJeu[0][-1] > self.plateauDeJeu[1][-1] :   
                    print("joueur 1 gagnant")
                    print("---------------")
                    self.joueur1.mainDuJoueur.append(self.plateauDeJeu[0])
                    self.joueur1.mainDuJoueur.append(self.plateauDeJeu[1])


            

        #cartes restantes
        print("---------------")
        print("Le joueur 1 a " + str(len(self.joueur1.mainDuJoueur)) + "cartes")
        print("Le joueur 2 a " + str(len(self.joueur2.mainDuJoueur)) + "cartes")
        print("total de cartes = " + str(len(self.joueur2.mainDuJoueur)+len(self.joueur1.mainDuJoueur)))

        #time.sleep(1)

    def joueurUnePartie(self, jeuDeCarte, joueur1, joueur2):
        self.distribuer(self.jeuDeCarte.paquet, self.joueur1, self.joueur2)
        totalCarteJoueur1 = len(self.joueur1.mainDuJoueur)
        totalCarteJoueur2= len(self.joueur2.mainDuJoueur)

        while totalCarteJoueur1 >= 0 or totalCarteJoueur2 >= 0:
            self.jouerUneManche(jeuDeCarte, joueur1, joueur2)



    

class joueur : 
    def __init__(self):
        self.mainDuJoueur=[]
    def



def oldMain():
    jeu = jeuDeCarte()
    #print(jeu.paquet)
    # print(jeu.paquet)
    jeu.melangePaquet(jeu.paquet)
    #print(jeu.paquet)

#CREATION DE LA PARTIE
    partieEnCours = partie(jeuDeCarte(), joueur(), joueur())
    #print(partieEnCours.jeuDeCarte.paquet)
    
#DISTRIBUTION DES CARTES
    partieEnCours.distribuer(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2)
    
#AFFICHAGE CARTE DISTRIBUEE
    # print("main du joueur 1")
    # print(len(partieEnCours.joueur1.mainDuJoueur))
    # print(partieEnCours.joueur1.mainDuJoueur)
    # print("main du joueur 2")
    # print(len(partieEnCours.joueur2.mainDuJoueur))
    # print(partieEnCours.joueur2.mainDuJoueur)
    # print("paquet")
    # print(partieEnCours.jeuDeCarte.paquet)


    #print(partieEnCours.plateauDeJeu)


    print(partieEnCours.joueur1.mainDuJoueur)
    print("Le joueur 1 a " + str(len(partieEnCours.joueur1.mainDuJoueur)) + "cartes")
    print("---------------")
    print(partieEnCours.joueur2.mainDuJoueur)
    print("Le joueur 2 a " + str(len(partieEnCours.joueur2.mainDuJoueur)) + "cartes")


    #description d'une manche 
    #partieEnCours.plateauDeJeu = (partieEnCours.joueur1.mainDuJoueur.pop(),partieEnCours.joueur2.mainDuJoueur.pop())


    #description du cas d'égalité 
    partieEnCours.plateauDeJeu = ((1,"coeur", "As de Coeur"), ((1,"coeur", "As de Coeur")))



    print("Joueur 1 joue : " + partieEnCours.plateauDeJeu[0][2]+" contre " + "joueur 2 joue : " + partieEnCours.plateauDeJeu[1][2]) 
    #règles du jeu
    if partieEnCours.plateauDeJeu[0][0] < partieEnCours.plateauDeJeu[1][0] :   
        print("joueur 2 gagnant")
        partieEnCours.joueur2.mainDuJoueur.append(partieEnCours.plateauDeJeu[0])
        partieEnCours.joueur2.mainDuJoueur.append(partieEnCours.plateauDeJeu[1])
    elif partieEnCours.plateauDeJeu[0][0] > partieEnCours.plateauDeJeu[1][0] :   
        print("joueur 1 gagnant")
        partieEnCours.joueur1.mainDuJoueur.append(partieEnCours.plateauDeJeu[0])
        partieEnCours.joueur1.mainDuJoueur.append(partieEnCours.plateauDeJeu[1])
    else : 
        print('égalité')
        totalCarteJoueur1 = len(partieEnCours.joueur1.mainDuJoueur)
        totalCarteJoueur2= len(partieEnCours.joueur2.mainDuJoueur)

        while totalCarteJoueur1 >= 0 or totalCarteJoueur2 >= 0:
            if totalCarteJoueur1 == 0:
                print("joueur 1 a perdu")
            elif totalCarteJoueur2 == 0:
                print("joueur 2 a perdu")
            else : 
                partieEnCours.plateauDeJeu = (partieEnCours.joueur1.mainDuJoueur.pop(),partieEnCours.joueur2.mainDuJoueur.pop())
        
        #######################################################GÉRER LE CAS DES ÉGALITÉS
    
    print(partieEnCours.joueur1.mainDuJoueur)
    print("Le joueur 1 a " + str(len(partieEnCours.joueur1.mainDuJoueur)) + "cartes")
    print("---------------")
    print(partieEnCours.joueur2.mainDuJoueur)
    print("Le joueur 2 a " + str(len(partieEnCours.joueur2.mainDuJoueur)) + "cartes")

    #print(partieEnCours.jeuDeCarte.paquet)

    #joueur1 = joueur()
    #joueur1.mainDuJoueur


def main():
    partieEnCours = partie(jeuDeCarte(), joueur(), joueur())
    partieEnCours.distribuer(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2)
    partieEnCours.joueurUnePartie(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2)


if __name__=='__main__':
    main()