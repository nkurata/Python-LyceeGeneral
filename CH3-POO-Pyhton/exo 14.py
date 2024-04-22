class Fraction:
    
    def __init__(self,n,d):
        if d <=0:
            raise ValueError("Mettez un nombre entier positif!")
        self.num=n
        self.denum=d
    
    def __str__(self):
        if self.denum==1:
            return str(self.num)
        return (str(self.num)+"/"+str(self.denum))
    
    def __eq__(self,u):
        return(self.num*u.denum == u.num*self.denum)
        
    def __lt__(self,u):
       return(self.num*u.denum < u.num*self.denum)
    
    def __add__(self,u):
        n = (self.num * u.denum) + (u.num * self.denum)
        d = self.denum * u.denum
        return Fraction(n,d)
    
    def __mul__(self,u):
        n = self.num * u.num
        d = self.denum * u.denum
        return Fraction(n,d)

#--------------------Programme Principale--------------------#
f=Fraction(4,3)
g=Fraction(4,1)
h=Fraction(8,6)
i=Fraction(5,2)

assert f.num == 4
assert f.denum == 3
assert f == h
assert str(f) == "4/3"
assert str(g) == "4"
assert f != g
assert f < i
assert f + i == Fraction(23, 6)
assert f * i == Fraction(20,6)

