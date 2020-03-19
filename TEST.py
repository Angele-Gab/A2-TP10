class Etudiant:
    def __init__(self, d, e):
        self.__devoir=d
        self.__exam=e
    def setDevoir(self, d):
        if d<0:
            print("erreur")
        else:
            self.__devoir = d
    def setExam(self, e):
        if e<0:
            print("erreur")
        else:
            self.__exam = e
    def getExam(self):
        return self.__exam

obj = Etudiant(15,16)
print("Exam =", obj.getExam())
