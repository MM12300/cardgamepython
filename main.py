import random

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
    

class joueur : 
    def __init__(self):
        self.mainDuJoueur=[]



def main():
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
    partieEnCours.plateauDeJeu = (partieEnCours.joueur1.mainDuJoueur.pop(),partieEnCours.joueur2.mainDuJoueur.pop())



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
        #######################################################GÉRER LE CAS DES ÉGALITÉS
    
    print(partieEnCours.joueur1.mainDuJoueur)
    print("Le joueur 1 a " + str(len(partieEnCours.joueur1.mainDuJoueur)) + "cartes")
    print("---------------")
    print(partieEnCours.joueur2.mainDuJoueur)
    print("Le joueur 2 a " + str(len(partieEnCours.joueur2.mainDuJoueur)) + "cartes")


   
   
   
    #print(partieEnCours.jeuDeCarte.paquet)

    #joueur1 = joueur()
    #joueur1.mainDuJoueur





if __name__=='__main__':
    main()