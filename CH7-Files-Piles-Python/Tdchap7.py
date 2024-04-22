# Créé par kuratan, le 18/11/2021 en Python 3.7
from Pile import *
courante=""
precedentes=Pile()

def aller_a(cible):
    global courante
    if courante !="":
        precedente.empiler(courante)
    courante=cible
    suivantes=Pile()

def retour_arriere():
    global courante
    if not precedente.est_vide():
        courante=precedent.depiler()
        
def retour_avant():
    global courante
    if not suivantes.est_vide():
        precedentes.empiler(courante)
        courante=suivantes.depiler()
        
