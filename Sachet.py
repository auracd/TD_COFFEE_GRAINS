import Grain

class Sachet(): 

    def __init__(self, poids, type, grains, compo):
        self.poids = poids
        self.type = type
        self.liste_grains = grains
        self.compo_grains = compo
    

    def is_valid(self) : 
        t = ["pure", "mixte"] 
        tValid = self.type in t

        if(self.type in t == "pure") : 
            self.liste_grains.len = 1
            self.compo_grains = 100 
        
        pValid = False
        if(self.poids >= 500 and self.poids <= 2000 and self.poids % 500 == 0) : 
            pValid = True
        
        cValid = False 
        
        if (sum(self.compo_grains) == 100) :
            cValid = True 

        return tValid and pValid and cValid
    
        