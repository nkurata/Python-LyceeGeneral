
class Liste:
    """Une liste chainée"""

    def __init__(self):
        """contient un attribut 'tete' qui est un objet
            Cellule qui définit la 'tete' de la liste"""
        self.tete=None

    def ajoute (self, v):
        """ajoute v en tete de liste"""
        self.tete=Cellule(v,self)

    def est_vide(self):
        """renvoie True si la tete est vide, False sinon"""
        return self.tete is None

    def tete(self):
        """renvoie la tete de la liste"""
        return self.tete.valeur

    def queue(self):
        """renvoie la liste si on retire la tete"""
        return self.tete.suivante

    def __str__(self):
        return str(self.tete)

    def __len__(str):
        """return la longueur de la liste"""
        return longueur(self.tete)

    def __getitem__(self, n):
        return nieme_element(n, self.tete)

    def __add__(self, lst):
        return concatener(self.tete, lst.tete)

    def reverse(self):
        return inverse(self.tete)


class Cellule:
    """Une cellule contient 1 valeure et un autre objet de type cellule (stocké dans 'suivant')"""
    def __init__(self,v,s):
        self.valeur=v
        self.suivante=s

    def __str__(self):
        """affiche Cellule(3, Cellule(5, Cellule(2,None)))"""
        if self is None:
            return " "
        if self.suivante is None:
            return str(self.valeur)
        return str(self.valeur)+" "+ str(self.suivante)

def longueur(cel):
    """renvoie la longueur de la liste"""
    if cel is None:
        return 0
    return 1+longueur(cel.suivante)

def nieme_element(n,cel):
    """renvoie la valeur de la nieme celulle le rang 0"""
    if cel is None or n<0:
        return None
    if n==0:
        return cel.suivante
    return nieme_element(n-1, cel.suivante)

def concatener(l1, l2):
    """concatene l1 et l2 pus renvoie une nouvelle liste"""
    if l1 is None:
        return l2
    return Cellule(l1.valeur, concatener(l1.suivante, l2))

def inverse(cel):
    """ inverse l'ordre de cellules et renvoie une nouvelle celulle"""
    inv=None
    c=cel
    while c is not None:
        inv=Cellule(c.valeur, inv)
        c=c.suivante
    return inv


l = Cellule(3, Cellule(5, Cellule(2, None)))
l0 = Cellule(6, Cellule(1, Cellule(4, None)))
assert str(l) == "3 5 2"
assert longueur(l) ==  3
assert nieme_element(2, l) == Cellule(5, Cellule(2, None))
assert concatener(l, l0) == Cellule(3, Cellule(5, Cellule(2, Cellule (6, Cellule(1, Cellule(4, None))))))
assert inverse(l) ==  Cellule(2, Cellule(5, Cellule(3, None)))
