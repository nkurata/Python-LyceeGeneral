def applique(f,t):
    """renvoie un nouveau tableau de meme taille ou la fonction f a été appliqué a chaque element de t"""
    if t == []:
        return None
    if len(t) == 1:
        return t[0] + [f]
     
    
    



assert(lambda x: x+4, [2,3,4]) == [6,7,8]   