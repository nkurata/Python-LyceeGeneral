def boucle(i,k):
    if i == k:
        return k
    else:
        return (i,boucle(i+1,k))
assert boucle(2,2)==2
assert boucle(1,2)==(1,2)