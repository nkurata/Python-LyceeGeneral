# Créé par kuratan, le 18/11/2021 en Python 3.7
class pile:
    """ une structure de pile"""
    def __init__(self):
        """coutenu est la cellule au sommet de la pile"""
        self.coutenu=None

    def est_vide(self):
        return self.contenu is None

    def empiler(self):
        self.contenu=Cellule(e, self.contenu)

    def depiler(self):
        a_depiler=self.contenu.valeur
        self.contenu=self.contenu.suivante
        return a_depiler
