#Exercice 14
class Fraction:
    def __init__ (self, num, denom):
        self.num = num
        self.denom = denom
        if denom <= 0:
            raise ValueError("denominateur"+str(denom)+"invalide")
    
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        if self.denom > 1:
            return (str(self.num), "/", str(self.denom))
        

f=Fraction(5,7)
    
    
