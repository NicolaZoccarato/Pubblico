class Maillon(object):
    def __init__(self, donnee):
        self.__donnee = donnee
        self.__suivant = None

    @property
    def donnee(self):
        return self.__donnee
    
    @donnee.setter
    def donnee(self, value):
        self.__donnee = value

    @property
    def suivant(self):
        return self.__suivant

    @suivant.setter
    def suivant(self, value):
        if not isinstance(value, Maillon) and value is not None:
            raise TypeError("Le suivant doit etre un maillon!")
        else:
            self.__suivant = value

    def __str__(self):
        return "Maillon (%s, suivant %s)" % (str(self.donnee), repr(self.suivant))


class LC(object):
    def __init__(self, premier=None):
        self.premier = premier
        self.__taille = 0

    @property
    def premier(self):
        return self.__premier

    @premier.setter
    def premier(self, maillon):
        if not isinstance(maillon, Maillon) and maillon is not None:
            raise TypeError("Le premier doit etre un maillon!")
        else:
            self.__premier = maillon
    
    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, value):
        if value is not int:
            raise TypeError("Il faut entrer un integer!")
        else:
            self.__taille = value

    def estVide(self):
        if self.premier is None:
            return True
        else:
            return False

    def supprimerPremier(self):
        if self.estVide == True:
            raise TypeError("La liste est déjà vide!")
        else:
            self.premier = self.premier.suivant
            self.taille -= 1

    def vider(self):
        self.premier = None
        self.taille = 0

    def ajouterEnTete(self, x):
        tete = Maillon(x)
        tete.suivant = self.premier
        self.premier = tete
        self.taille += 1

    def ajouterApres(self, x, y):
        if list.estVide() == True:
            raise TypeError("La liste est vide!")
        else:
            nuveauMaillon = Maillon(x)
            maillon = self.premier
            while maillon.donnee != y:
                if maillon.suivant is None:
                    raise TypeError("La liste ne contien pas y!")
                maillon = maillon.suivant
            nuveauMaillon.suivant = maillon.suivant
            maillon.suivant = nuveauMaillon
            self.taille += 1

    def supprimerSuivant(self, x):
        if list.estVide() == True:
            raise TypeError("La liste est vide!")
        else:
            maillon = self.premier
            while maillon.donnee != x:
                if maillon.suivant is None:
                    raise TypeError("La liste ne contien pas y!")
                maillon = maillon.suivant
            maillon2 = maillon.suivant
            maillon.suivant = maillon2.suivant
            self.taille -= 1

    def __len__(self):
        return self.taille
        #if self.estVide() == True:
        #    return 0
        #else:
        #    maillon = self.premier
        #    length = 1
        #    while maillon.suivant is not None:
        #        maillon = maillon.suivant
        #        length += 1
        #    return length

    def __str__(self):
        if list.estVide() == True:
             return "La liste est vide"
        else:
            maillon = self.premier
            while maillon.suivant is not None:
                print("Maillon (%s, suivant %s)" % (str(maillon.donnee), repr(maillon.suivant.donnee)))
                maillon = maillon.suivant
            return "Maillon (%s, suivant None)" % (str(maillon.donnee))




list = LC()
list.ajouterEnTete(3)
list.ajouterApres(2,3)
list.supprimerSuivant(3)
print(len(list))
print(list)