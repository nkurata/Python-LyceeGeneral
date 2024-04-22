
################### Jeu de Lemmings ###################

"""
Répartition des taches
Neïl = 
Noé = 
"""
class NnJeu:
    """Definit une classe Jeu contenant un tableau a deux dimensions de cases et un
        attribut lemming contenant un tableau de lemming actuellement en jeu # = mur 0 = sortie"""
    
    def __init__(self, c):
        """initialise la classe Jeu et ces attributs"""
        c = open('carte1.txt') #import la carte dans le meme fichier
        self.grotte = [[NnCase(terrain) for terrain in ligne if terrain != '\\n'] for ligne in c.readlines()]
        c.close() #ferme la carte si le terrain n'est pas complet
        self.lemmings = [] #cree un tableau vide pour les lemmings

    def __getitem__(self, i):
        """méthode qui permet d'accéder à la ligne i du grotte
            directement à partir d’une instance J avec la notation J[i]"""
        return self.grotte[i] 

    def affiche(self):
        """affiche la carte avec les positions de tous les lemmings du jeu"""
        for ligne in self.grotte:
            for case in ligne:
                print(case, end='')
        print()

    def ajoute_lemming(self) :
        """ ajoute un lemming si la case 0,1 est libre """
        if self.grotte[0][1].libre():
            lem = NnLemming(self, 0, 1)
            self.lemmings.append(lem)
        self.grotte[0][1].arrivee(lem)

    def tour(self):
        """fait agir chaque lemming une fois et affiche le nouvel etat du jeu"""
        for lem in self.lemmings[:]:
            lem.action()

    def demarre(self):
        """lance une boucle infini attendant des commandes de l'utilisateur"""
        while True:
            comand = input()
            if comand == 'q':
                break
            elif comand == 'l':
                self.ajoute_lemming()
            else:
                self.tour()
                self.affiche()
                
class NnLemming:
    
    """ Déffinit une class lemming avec des attributs positifs l = la ligne,c = la colonne auxquelles
        se trouve le lemming, d = 1 pour aller a droitre et -1 pour aller a gauche"""
    
    def __init__(self,J,l,c):
        """innitialise les attributs utiliser dans cet class"""
        self.J = J
        self.l = l
        self.c = c
        self.d = 1
    
    
    def __str__(self):
        """renvoie '>' ou '<' selon la direction du lemming"""
        if self.d > 0:
            return ('>')
        else:
            return ('<')
        
    def mouvement (self, l, c):
        """déplacer le lemming vers la case de coordonnées (1, c)  si la case est libre"""
        if not self.J[l][c].libre():
            return False
        self.J[self.l][self.c].depart()
        self.J[l][c].arrivee(self)
        return True
    
    def action(self):
        """ tombe si la case dessous et vide, se retourne si il touche le mur"""
        if self.mouvement(self.l+1, self.c):
            self.l += 1
        elif self.mouvement(self.l, self.c + self.d):
            self.c += self.d
        else:
            self.d = -self.d

    def sort(self):
        """ retire le lemming du jeu"""
        self.J.lemmings.remove(self)
        

        
class NnCase:
    """contient un attribut terrain contenant le caractere representant la caracteristique
        de la case(mur, vide, sortie), et un attribut lemming"""
        
    def __init__(self, terrain):
        """ initialise la class Case et ses attributs"""
        self.terrain = terrain
        self.lem = None

    def __str__(self):
        """renvoie le caractere a afficher pour representer cette case ou
            son eventuel occupant"""
        if self.lem is not None:
            return str(self.lem)
        else:
            return self.terrain
        
    def libre(self):
        """renvoie True si la case peut recevroir un lemming (ni un mur, ni occupee)"""
        return (self.terrain == ' ' or self.terrain == '0')
    
    def depart(self):
        """retire le lemming present"""
        self.lem = None

    def arrivee(self, lem):
        """place le lemming lem sur la case ou le fait sortir du jeu
            si la case etait une sortie"""
        if self.terrain == '0':
            lem.sort()
        else:
            self.lem = lem
        
        
NnJeu('carte1.txt').demarre() #instance du jeu qui donne le nom du fichier texte et appel sa methode de depart
    
    

        