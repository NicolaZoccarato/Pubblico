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

    def __lt__(self, x):
        return self.donnee < x.donnee



class itLC():
    def __init__(self, list):
        self.__list = list
        self.__position = len(list)
    def __iter__(self):
        self.i = list.premier
        return self
    def __next__(self):
        next = self.i
        self.i = self.i.suivant
        return next
    #def __next__(self):
    #    if self.__position == 0:
    #        raise StopIteration
    #    self.__position += 1
    #    return self.__list[self.__position]



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
        try:
           value = int(value)
        except ValueError:
            raise TypeError("Il faut entrer un integer!")
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

    def ajouterEnTete(self, x):         #From the text of the exercise I understood that x should be the content of a node, not a Maillon-type object. The same for ajouterApres and supprimerSuivant
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

    def __iter__(self):
        return itLC(self)

    def inserer(self, elt, debut = None):       #I suppose growing order of the nodes. "debut" is the content of a node.
        if debut is None:
            maillon = self.premier.suivant
        else:
            iterator = itLC(self)
            for m in iterator:
                if m.donnee == debut:
                    maillon = m.suivant
                    break
        x = Maillon(elt)
        while maillon.suivant is not None:
            if maillon < x:
                x.suivant = maillon.suivant
                maillon.suivant = x
            else:
                maillon = maillon.suivant
                
            


list = LC()
list.ajouterEnTete(2)
list.ajouterApres(3,2)
list.ajouterApres(5,3)
list.inserer(4,2)
print(len(list))
print(list)