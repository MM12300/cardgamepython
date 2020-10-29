import partie
import joueur
import jeuDeCarte

def main():
    partieEnCours = partie.partie(jeuDeCarte.jeuDeCarte(), joueur.joueur(), joueur.joueur())
    partieEnCours.distribuer(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2)
    partieEnCours.joueurUnePartie(partieEnCours.jeuDeCarte.paquet, partieEnCours.joueur1, partieEnCours.joueur2,0)


if __name__=='__main__':
    main()