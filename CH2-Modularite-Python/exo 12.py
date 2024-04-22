#Exercice 12
def tranche(t,i,j):
    """Renvoie un nouveau tableau contenant les elements de t de l'indice i
        inclus a l'indice a l'indice j exclu (et le tableau vide si j<=i"""
    if j<=i:
        return []
    else:
        nv_tab = [0]*(j-i)
        for k in range(i,j):
            nv_tab[k-i] = t[k]
        return nv_tab

"""def concatenation(t1, t2):
    ""Renvoie un nouveau tableau contenant, dans
    l'orde, les éléments de t1 puis les éléments de t2""
    nv_tab= t1,t2"""