def trouve(p,t):
    """renvoie le premier élément x de tel que p(x) vaut True si non renvoie None"""
    for i in range (len(t)):
        if p(t[i]) == True:
            return t[i]
    return None

assert not trouve(lambda x: x%2 == 0, [3,5,1])
assert trouve (lambda x: x%2 == 0, [2,5,1])
assert trouve (lambda x: type(x) == str, [3,"b",-2])
assert not trouve(lambda x: x%2 == 0, [])