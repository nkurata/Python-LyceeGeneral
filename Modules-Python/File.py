class File:
    """une structure de file"""
    
    def __init__(self):
        """crée une file vide, si la file est vide, ou si elle contient un seul element la tete et la queue se confondent"""
        self.tete=None
        self.queue=None
        
        def est_vide(self):
            return self.tete is None
        
        def enfiler(self,e):
            c=Cellule(e, None)
            if self.est_vide():
                self.tete=c
            else:
                self.queue.suivante=c
            self.queue=c
        
        def defiler(self):
            if self.est_vide():
                return None
            temp=self.tete.valeur
            self.tete=self.tete.suivante
            return temp
        
            