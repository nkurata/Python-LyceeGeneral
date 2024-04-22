from random import shuffle
class Carte:
    """ une carte de jeu de 32 carte"""
    def __init__(self, v, c):
        figures = ('7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')
        self.valeur = v
        self.couleur = c
        self.figures = figures[self.valeur -7 ]
        
    def __str__(self):
        return self.figures + " de " + self.couleur
    
class Jeu:
    """Un jeu de 32 cartes"""
    def __init__ (self):
        couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
        valeurs = (7, 8, 9, 10, 11, 12, 13, 14)
        self.paquet = []
        for c in couleurs :
            for v in valeurs :
                self.paquet.append(Carte(v,c))
    
    def melange(self):
        shuffle(self.paquet)
    
    def distribue(self):
        j1 = []
        j2 = []
        for _ in range(16):
            j1.append(self.paquet.pop())
            j2.append(self.paquet.pop())
        return j1, j2
    
class Joueur:
    """un joueur de cartes"""
    
    def __init__(self):
        self.paquet = []
    
    def perdu(self):
        return self.paquet = []
    
    def tirer(self):
        if len(self.paquet) > 0:
            return self.paquet.pop(0)

class Bataille:
    """ jeu de bataille payante. En cas d'egalité, chacun perd ca classe"""
    
    def __init__(self, j1, j2, j):
        self.joueur1=j1
        self.joueur2=j2
        self.jeu=j
        
    def manche(self):
        carte_joueur1 = self.joueur1.tirer()
        carte_joueur2 = self.joueur2.tirer()
        if carte_joueur1.valeur > carte_joueur2.valeur:
            self.joueur1.jeu.append(carte_joueur1)
            self.joueur1.jeu.append(carte_joueur2)
            if self.joueur2.jeu != []:
                slef.joueur1.jeu.append(self.joueur2.jeu.pop())
            
        elif carte_joueur1.valeur < carte_joueur2.valeur:
            self.joueur2.jeu.append(carte_joueur2)
            self.joueur2.jeu.append(carte_joueur1)
            if self.joueur1.jeu != []:
                self.joueur2.jeu.append(self.joueur1.jeu.pop())
        
        return "Noé : " str(carte_joueur1) + " - Sarah :" str(carte_joueur2)
    
            