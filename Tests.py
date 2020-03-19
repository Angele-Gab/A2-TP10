from Multinationale import *
from Filiale import *
from Salariés import *

Premiere = Multinationale("RCAT"," la France")
F1 = Filiale("RCAT-Belgique","Belgique",1000)
F2 = Filiale("RCAT-Maroc", "Maroc", 1492)
F3 = Filiale("RCAT-Tunisie", "Tunisie", 1515)
F4 = Filiale("RCAT-Angleterre", "Angleterre", 1789)

Premiere.Ajout (F1)
Premiere.Ajout (F2)
Premiere.Ajout (F3)
Premiere.Ajout (F4)

S1 = Directeur("Colomb", "Christophe", 7, 121, 1516)
F3.AjoutSalarie(S1)
S2 = Senior("Medicis", "Catherine", 5, 100,1517,12,11,1,"Café")
F3.AjoutSalarie(S2)
S3 = Junior("César","Jules", 5, 123,1037,23,1,22,34)
F1.AjoutSalarie(S3)
S4 = Administratif("Polo", "Marco", 3, 134,167,23,"Fiesta")
F1.AjoutSalarie(S4)
S5 = Senior("Vespucci", "Amerigo", 4, 234,1500,14,11,3,"Ambiance")
F2.AjoutSalarie(S5)
Premiere.Affichage()

