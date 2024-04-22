#------------------- Poisson -------------------#
import random

class Case:
    
    def __init__(self, terrain):
        self.terrain = terrain
        self.ps = None
    
    def __str__(self):
        if self.ps is not None:
            return str(self.ps)
        else:
            return self.terrain
        
    def libre(self):
        return (self.terrain == ' ')
        
class Aquarium:
    """Definit une classe Aquarium a deux dimmensions (longueur, largeur) avec # = bordure"""
    
    def __init__(self,aq):
        """initialise la class Aquarium et ses variables"""
        aq = open('aquarium1.txt')
        self.aqua = [[Case(terrain) for terrain in ligne if terrain != '\\n'] for ligne in aq.readlines()]
        aq.close() 
        self.poissons = []
    
    def __getitem__(self, i):
        return self.aqua[i] 
    
    def affiche(self):
        """affiche les poissons dans la carte"""
        for ligne in self.aqua:
            for c in ligne:
                print(c, end='')
        print()
    
    def ajoute_Poisson(self) :
        """ajoute un poisson dans une case aleatoire"""
        if self.aqua[random.randint(1,11)][random.randint(1,11)].libre():
            ps = Poisson(self, random.randint(1,11), random.randint(1,11))
            self.poissons.append(ps)
        return None
                    
    def tour(self):
        """fais tourner le code et affiche les resultats 1 par 1"""
        for ps in self.poissons[:]:
            ps.mouvement()
            
    def demarre(self):
        """demarre le code et ajoute un total de 11 poissons"""
        i = 1
        while i <= 11:
            self.ajoute_Poisson()
            i += 1
                    
class Poisson:
    
    def __init__(self, a, l, c):
        self.a = a
        self.l = l
        self.c = c
        self.direction = 1
                    
    def __str__(self):
        if self.direction > 0:
            return ('>')
        else:
            return ('<')
        
    def mouvement(self, l, c):  
        """ poisson se retourne si il touche un mur ou un autre poisson """
        if self.a[l][c].libre():
            if self.mouvement(self.l+1, self.c):
                self.l += 1
        if not self.a[l][c].libre():
            self.diretion = -self.direction
        
    
                    
                    
                    
Aquarium('aquarium1.txt').demarre()    