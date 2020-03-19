from Multinationale import *
class Filiale :

    def __init__(self, Nom, Pays, DateCreation, ListeSalaries=[]) :
        self.__N = Nom
        self.__Pays = Pays
        self.__Date = DateCreation
        self.__LS = ListeSalaries

    def getCreation (self) :
        return self.__Date

    def getNom (self) :
        return self.__N

    def getLS (self) :
        return self.__LS

    def getPays (self) :
        return self.__Pays

    def AjoutSalarie(self,d):
        self.__LS.append(d)

    def Suppression(self,d):
        self.__LS.remove(d)

    def Affichage(self, ListeSalaries):
        print("Site : ", self.__Pays)
