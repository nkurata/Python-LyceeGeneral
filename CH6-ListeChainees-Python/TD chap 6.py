from Liste import *
#TD chap 6
#2



def listeN(n):
    """reçoit en argument un entier n ositif ou nul et renvoie une liste chaînée des entiers 1, 2,...n, dans cet ordre"""
    if n==0:
        return None
    if n==1:
        return Cellule(1,None)
    return Cellule(listeN(n-1),Cellule(n,None))
assert str(listeN(5)) == '1 2 3 4 5'
#3
#def occurences(x, lst):
    