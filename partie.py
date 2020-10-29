import time
import sys
import joueur as joueur


#Représente une partie carte avec un jeu de carte et 2 joueurs
#Méthodes : 
# - distribuer(self, jeuDeCarte, joueur1, joueur2) : permet de distribuer les cartes du paquet une à une entre les 2 joueurs, en commençant toujours par le joueur 2 (il obtient tjrs la première carte du paquet)
# - regle(self, jeuDeCarte, joueur1, joueur2) : règle du jeu, ici la bataille
# - jouerUneManche(self, jeuDeCarte, joueur1, joueur2) : représente le déroulement d'une manche
# - joueurUnePartie(self, jeuDeCarte, joueur1, joueur2) : représente le déroulement de la partie entière
class partie : 
    def __init__(self, jeuDeCarte, joueur1, joueur2) : 
        self.jeuDeCarte = jeuDeCarte
        self.joueur1 = joueur.joueur()
        self.joueur2 = joueur.joueur()
        self.plateauDeJeu=[]

    def distribuer(self, jeuDeCarte, joueur1, joueur2):
        self.jeuDeCarte.melangePaquet(self.jeuDeCarte.paquet)
        for n in range(len(self.jeuDeCarte.paquet)):
            if n % 2 == 0 : 
                self.joueur1.getMainDuJoueur().append(self.jeuDeCarte.paquet.pop())
            else:
                self.joueur2.getMainDuJoueur().append(self.jeuDeCarte.paquet.pop())

    def regle(self, jeuDeCarte, joueur1, joueur2):
        totalCarteJoueur1 = len(self.joueur1.getMainDuJoueur())
        totalCarteJoueur2= len(self.joueur2.getMainDuJoueur())
        
        if totalCarteJoueur1 == 0 :
            self.joueur2.getMainDuJoueur().append(self.plateauDeJeu[0])
            self.joueur2.getMainDuJoueur().append(self.plateauDeJeu[1])
            print("Le joueur 1 a " + str(len(self.joueur1.getMainDuJoueur())) + "cartes")
            print("---------------")
            print("Le joueur 2 a " + str(len(self.joueur2.getMainDuJoueur())) + "cartes")
            print("")
            sys.exit('le joueur 2 a gagné ! Bravo')
        elif totalCarteJoueur2 == 0 : 
            self.joueur1.getMainDuJoueur().append(self.plateauDeJeu[0])
            self.joueur1.getMainDuJoueur().append(self.plateauDeJeu[1])
            print("Le joueur 1 a " + str(len(self.joueur1.getMainDuJoueur())) + "cartes")
            print("---------------")
            print("Le joueur 2 a " + str(len(self.joueur2.getMainDuJoueur())) + "cartes")
            print("")
            sys.exit('le joueur 1 a gagné ! Bravo')

        else : 
            if self.plateauDeJeu[0][-1] == self.plateauDeJeu[1][-1] :
                self.plateauDeJeu = (self.joueur1.getMainDuJoueur().pop(),self.joueur2.getMainDuJoueur().pop())
                self.plateauDeJeu = (self.joueur1.getMainDuJoueur().pop(),self.joueur2.getMainDuJoueur().pop())
                
            else :
                if self.plateauDeJeu[0][-1] < self.plateauDeJeu[1][-1] :   
                    print("Le joueur 2 gagne cette manche")
                    print("")
                    self.joueur2.getMainDuJoueur().append(self.plateauDeJeu[0])
                    self.joueur2.getMainDuJoueur().append(self.plateauDeJeu[1])
                elif self.plateauDeJeu[0][-1] > self.plateauDeJeu[1][-1] :   
                    print("Le joueur 1 gagne cette manche")
                    print("")
                    self.joueur1.getMainDuJoueur().append(self.plateauDeJeu[0])
                    self.joueur1.getMainDuJoueur().append(self.plateauDeJeu[1])


    def jouerUneManche(self, jeuDeCarte, joueur1, joueur2, tempsAttenteEntreDeuxManches):
        print("État actuel du jeu :")
        print("")
        print("Le joueur 1 a " + str(len(self.joueur1.getMainDuJoueur())) + "cartes")
        print("---------------")
        print("Le joueur 2 a " + str(len(self.joueur2.getMainDuJoueur())) + "cartes")
        print("")

        print("Attention... on joue !")
        self.plateauDeJeu = (self.joueur1.getMainDuJoueur().pop(),self.joueur2.getMainDuJoueur().pop())
        print("Joueur 1 (" + self.plateauDeJeu[0][2]+") contre " + "Joueur 2 (" + self.plateauDeJeu[1][2] + ")") 

        self.regle(self.jeuDeCarte, self.joueur1, self.joueur2)


        #cartes restantes
        print("---------------")
        print("Le joueur 1 a " + str(len(self.joueur1.getMainDuJoueur())) + "cartes")
        print("Le joueur 2 a " + str(len(self.joueur2.getMainDuJoueur())) + "cartes")
        print("Total de cartes = " + str(len(self.joueur2.getMainDuJoueur())+len(self.joueur1.getMainDuJoueur())))
        print("FIN DE LA MANCHE")
        print("")

        time.sleep(tempsAttenteEntreDeuxManches)

    def joueurUnePartie(self, jeuDeCarte, joueur1, joueur2, tempsAttenteEntreDeuxManches):
        print("DÉBUT DE LA PARTIE !")
        self.distribuer(self.jeuDeCarte.paquet, self.joueur1, self.joueur2)
        totalCarteJoueur1 = len(self.joueur1.getMainDuJoueur())
        totalCarteJoueur2= len(self.joueur2.getMainDuJoueur())

        while totalCarteJoueur1 >= 0 or totalCarteJoueur2 >= 0:
            self.jouerUneManche(jeuDeCarte, joueur1, joueur2, tempsAttenteEntreDeuxManches)