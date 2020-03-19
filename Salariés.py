from Filiale import *
class Salarie :

    def __init__(self, Nom, Prenom, Salaire, Identifiant) :
        self._N = Nom
        self._P = Prenom
        self._S = Salaire
        self._Id = Identifiant

    def Affichage(self):
        pass


class Directeur (Salarie) :

    def __init__(self,Nom, Prenom, Salaire, Identifiant,AnneeNomination) :
        Salarie.__init__(self,Nom,Prenom,Salaire,Identifiant)
        self.__AN = AnneeNomination

    def Affichage(self):
        print("* [id=",self._Id,"] Nom et prénom : ", self._N, self._P,", Salaire : ",self._S," Statut : Directeur , Année de nomantion : ", self.__AN)

class Employe (Salarie) :

    def __init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail):
        Salarie.__init__(self,Nom, Prenom,Salaire,Identifiant)
        self._AE = AnneeEmbauche
        self._NbHT = NbHTravail

    def Affichage(self):
        pass

class Administratif (Employe) :

    def __init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail,Service):
        Employe.__init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail)
        self._Service = Service

    def Affichage(self):
        print("* [id=",self._Id,"] Nom et prénom : ", self._N, self._P,", Salaire : ",self._S,", Statut : Administratif, Année d'embauche : ",self._AE,", Nombre de jours de travail : ",self._NbHT," , Service : ", self._Service)

class Ingenieur (Salarie) :

    def __init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail,NbHProjet,NbHGestion) :
        Employe.__init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail)
        self._NbHP = NbHProjet
        self._NbHG = NbHGestion

    def Affichage(self):
        pass

class Junior (Ingenieur) :

    def __init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail,NbHProjet,NbHGestion,NbAnneeXP) :
        Ingenieur.__init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail,NbHProjet,NbHGestion)
        self.__NbAnXP = NbAnneeXP

    def Affichage(self):
        print("* [id=",self._Id,"] Nom et prénom : ", self._N, self._P,", Salaire : ",self._S,", Statut : Ingénieur Junior, Année d'embauche : ",self.AE, ",Nombre d'heure de projet : ", self.__NbHP, ", Nombre d'heure de gestion : ",self.__NbHG,", Nombre d'année d'expérience : ", self.__NbAnXP)

class Senior (Ingenieur):

    def __init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail,NbHProjet,NbHGestion,Responsabilite) :
         Ingenieur.__init__(self,Nom, Prenom, Salaire, Identifiant,AnneeEmbauche,NbHTravail,NbHProjet,NbHGestion)
         self.__Resp = Responsabilite

    def Affichage(self):
        print("* [id=",self._Id,"] Nom et prénom : ", self._N, self._P,", Salaire : ",self._S,", Statut : Ingénieur Junior, Année d'embauche : ",self.AE, ",Nombre d'heure de projet : ", self.__NbHP, ", Nombre d'heure de gestion : ",self.__NbHG, ", Responsabilité : ", self.__Resp)
