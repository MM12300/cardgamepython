import modules.partie as partie
import modules.joueur as joueur
import modules.jeuDeCarte as jeuDeCarte

  


def jouerUnePartie():
    #Création de la partie
    partieEnCours = partie.partie(jeuDeCarte.jeuDeCarte(), joueur.joueur(), joueur.joueur())
    #Distribution des cartes
    partieEnCours.distribuer(partieEnCours.jeuDeCarte.getPaquet(), partieEnCours.joueur1, partieEnCours.joueur2)
    #Début de la partie
    partieEnCours.joueurUnePartie(partieEnCours.jeuDeCarte.getPaquet(), partieEnCours.joueur1, partieEnCours.joueur2,1)


if __name__=='__main__':
    jouerUnePartie()