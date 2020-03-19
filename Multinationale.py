from Filiale import *
class Multinationale :

    def __init__(self, Nom, PaysOrigine, ListeFiliales=[]) :
        self.__Nom = Nom
        self.__PaysO = PaysOrigine
        self.__LF = ListeFiliales

    def Ajout(self,d):
        self.__LF.append(d)

    def getOrigine (self) :
        return self.__PaysO

    def getNom (self) :
        return self.__Nom

    def getLF (self) :
        return self.__LF

    def Affichage(self):
        NbFiliales = len(self.__LF)

        print("- La multinationale ", self.__Nom," est composée de ",NbFiliales," filiales. Son pays d'origine est ", self.__PaysO,".")
        ListeDates = []

        for j in self.__LF :
            DateVieille = self.__LF[0].getCreation()
            Ancienne = self.__LF[0]

            for i in self.__LF :
                if DateVieille > i.getCreation() :
                    Ancienne = i
                    Nom =Filiale.getNom()
                    ListeSalaries = Filiale.getLS
                    NbSalarie = len(ListeSalaries)
            print("La filiale la plus ancienne de cette multinationale de ", self.__PaysO," est : ", Nom,". Elle est composée de ",NbSalarie," salariés." )

        NbSalarie = len(ListeSalaries)

        print("- ", self.__Nom," est composé de ", NbSalarie," salariés.")


        for i in self.__LF :
            for j in i.getLS() :
                j.Affichage()
                i.Affichage()



        print("-----***-----")


