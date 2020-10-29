import time
import sys
import modules.joueur as joueur
import os


class plateauDeJeu:
    def __init__(self):
        self.plateauEnCours=[]

    def getPlateauEnCours(self) :
        return self.plateauEnCours

#Représente une partie carte avec un jeu de carte et 2 joueurs
#Méthodes : 
# - distribuer(self, jeuDeCarte, joueur1, joueur2) : permet de distribuer les cartes du paquet une à une entre les 2 joueurs, en commençant toujours par le joueur 2 (il obtient tjrs la première carte du paquet)
# - regle(self, jeuDeCarte, joueur1, joueur2) : règle du jeu, ici la bataille
# - jouerUneManche(self, jeuDeCarte, joueur1, joueur2) : représente le déroulement d'une manche
# - joueurUnePartie(self, jeuDeCarte, joueur1, joueur2) : représente le déroulement de la partie entière
class partie : 
    def __init__(self, jeuDeCarte, joueur1, joueur2, plateauDeJeu) : 
        self.jeuDeCarte = jeuDeCarte
        self.joueur1 = joueur.joueur()
        self.joueur2 = joueur.joueur()
        self.plateauDeJeu = plateauDeJeu()

    def distribuer(self, jeuDeCarte, joueur1, joueur2):
        self.jeuDeCarte.melangePaquet(self.jeuDeCarte.getPaquet())
        for n in range(len(self.jeuDeCarte.getPaquet())):
            if n % 2 == 0 : 
                self.joueur1.getMainDuJoueur().append(self.jeuDeCarte.getPaquet().pop())
            else:
                self.joueur2.getMainDuJoueur().append(self.jeuDeCarte.getPaquet().pop())

    #Règle du jeu de la bataille 
    def regle(self, jeuDeCarte, joueur1, joueur2, plateauDeJeu):
        totalCarteJoueur1 = len(self.joueur1.getMainDuJoueur())
        totalCarteJoueur2= len(self.joueur2.getMainDuJoueur())
        
        if totalCarteJoueur1 == 0 :
            #self.joueur2.getMainDuJoueur().append(self.plateauDeJeu[0])
            #self.joueur2.getMainDuJoueur().append(self.plateauDeJeu[1])
            print("")
            sys.exit('le joueur 2 a gagné ! Bravo!!!')
        elif totalCarteJoueur2 == 0 : 
            #self.joueur1.getMainDuJoueur().append(self.plateauDeJeu[0])
            #self.joueur1.getMainDuJoueur().append(self.plateauDeJeu[1])
            print("")
            sys.exit('le joueur 1 a gagné ! Bravo!!!')

        else : 
            self.plateauDeJeu.getPlateauEnCours().append(self.joueur1.getMainDuJoueur().pop())
            self.plateauDeJeu.getPlateauEnCours().append(self.joueur2.getMainDuJoueur().pop())

            plateau = self.plateauDeJeu.getPlateauEnCours()
            print(self.plateauDeJeu.getPlateauEnCours())
            print(plateau[0][0])
          
            #self.plateauDeJeu.plateauEnCours = [self.joueur1.getMainDuJoueur().pop(),self.joueur2.getMainDuJoueur().pop()]


            print("Joueur 1 (" + self.plateauDeJeu.plateauEnCours[0][2]+") CONTRE " + "Joueur 2 (" + self.plateauDeJeu.plateauEnCours[1][2] + ")") 


            if plateau[0][0] == plateau[1][0] :

                if totalCarteJoueur1 == 0 :
                    print("")
                    sys.exit('le joueur 2 a gagné ! Bravo!!!')
                elif totalCarteJoueur2 == 0 : 
                    print("")
                    sys.exit('le joueur 1 a gagné ! Bravo!!!')
                    print("BATAILLE ! ")



                plateau.insert(0,self.joueur1.getMainDuJoueur().pop())
                plateau.insert(0,self.joueur1.getMainDuJoueur().pop())

                print(self.plateauDeJeu.plateauEnCours)

                print("joueur 1")
                print(self.plateauDeJeu.plateauEnCours[0])
                print("joueur 2")
                print(self.plateauDeJeu.plateauEnCours[1])
                #time.sleep(10)
                
                #sys.exit('bataille')
                # self.plateauDeJeu = (self.joueur1.getMainDuJoueur().pop(),self.joueur2.getMainDuJoueur().pop())
                # self.plateauDeJeu = (self.joueur1.getMainDuJoueur().pop(),self.joueur2.getMainDuJoueur().pop())
            else :
                if plateau[0][0] < plateau[1][0] :   
                    print("Le joueur 2 gagne cette manche.")
                    print("")


                    for n in range(len(plateau)):
                        self.joueur2.getMainDuJoueur().insert(0, plateau.pop())

                    #for carte in plateau:
                        #self.joueur2.getMainDuJoueur().insert(0,carte)


                    #self.joueur2.getMainDuJoueur().insert(0,self.plateauDeJeu[0])
                    #self.joueur2.getMainDuJoueur().insert(1,self.plateauDeJeu[1])


                elif plateau[0][0] > plateau[1][0] :  

                    # for carte in plateau:
                    #     self.joueur1.getMainDuJoueur().insert(0,plateau.pop(carte))

                    for n in range(len(plateau)):
                        self.joueur1.getMainDuJoueur().insert(0, plateau.pop())

                    print("Le joueur 1 gagne cette manche.")
                    print("")

                    
                    # self.joueur1.getMainDuJoueur().insert(0,self.plateauDeJeu[0])
                    # self.joueur1.getMainDuJoueur().insert(1,self.plateauDeJeu[1])


    def jouerUneManche(self, jeuDeCarte, joueur1, joueur2, tempsAttenteEntreDeuxManches):
        os.system('cls||clear')
        print("DÉBUT DE LA MANCHE :")
        print("")
        print("Le joueur 1 a " + str(len(self.joueur1.getMainDuJoueur())) + "cartes")
        print("---------------")
        print("Le joueur 2 a " + str(len(self.joueur2.getMainDuJoueur())) + "cartes")
        print("")

        print("Attention... on joue !")
        




        # print("full plateau")
        # print(self.plateauDeJeu)
        # print("joueur 1")
        # print(self.plateauDeJeu[0])
        # print("joueur 2")
        # print(self.plateauDeJeu[1])
        # print(self.plateauDeJeu[0][-1])
        # print(self.plateauDeJeu[1][-1])





        





        self.regle(self.jeuDeCarte, self.joueur1, self.joueur2, self.plateauDeJeu)
    

        print("---------------")
        #permet de vérifier que le nombre de cartes est bien constant et donc qu'il n'y a pas de "bug"
        print("Total de cartes = " + str(len(self.joueur2.getMainDuJoueur())+len(self.joueur1.getMainDuJoueur())))
        print("FIN DE LA MANCHE")
        print("")

        time.sleep(tempsAttenteEntreDeuxManches)

    def joueurUnePartie(self, jeuDeCarte, joueur1, joueur2, tempsAttenteEntreDeuxManches):
        print("DÉBUT DE LA PARTIE !")
        self.distribuer(self.jeuDeCarte.getPaquet(), self.joueur1, self.joueur2)
        totalCarteJoueur1 = len(self.joueur1.getMainDuJoueur())
        totalCarteJoueur2= len(self.joueur2.getMainDuJoueur())

        while totalCarteJoueur1 >= 0 and totalCarteJoueur2 >= 0:
            self.jouerUneManche(jeuDeCarte, joueur1, joueur2, tempsAttenteEntreDeuxManches)