class Intervalle:
    
    def __init__(self,a,b):
        self.inf=a
        self.sup=b
        
    def est_vide(self):
        if self.sup < self.inf:
            return True
        else:
            return False
    
    def __len__(self):
        if self.sup < self.inf:
            return 0
        return self.sup - self.inf+1
    
    def __eq__ (self,u):
        if self.inf == u.inf and self.sup == u.sup:
            return True
        return False
    
    def __contains__(self, x):
        return x >= self.inf and x <= self.sup
    
    def __le__(self,u):
        if self.inf >=  u.inf and self.sup <= u.sup:
            return True
        return False

    
    
    
#----------------Programme Principale---------------#
i = Intervalle(9,5)
j = Intervalle(2,5)
k = Intervalle(4,8)
l = Intervalle(5,7)
assert i.est_vide()
assert len(j) == 4
assert Intervalle(9,5) == i
assert 5 in k
assert l <= k
#assert k.intersection(j) == Intervalle(4,5)
#assert k.union(j) == Intervalle(2,8)
#assert j <= k

