#Représente un joueur
#La main du joueur est privée (accessible via getter)
class joueur : 
    def __init__(self):
        self.__mainDuJoueur=[]

    def getMainDuJoueur(self):
      return self.__mainDuJoueur