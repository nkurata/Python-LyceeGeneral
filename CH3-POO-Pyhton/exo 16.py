class Angle:
    
    def __init__(self,angle):
        self.deg = angle % 360
        
    def __str__(self):
        return(str(self.deg) + "degrés")
    
    def ajoute
        