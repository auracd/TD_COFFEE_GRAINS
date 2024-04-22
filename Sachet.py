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
        gValid = True
        cValid = False 
        pValid = False

        if(self.type in t == "pure") : 
            if(self.liste_grains.len != 1): 
                gValid = False
            if(self.compo_grains == 100) : 
                cValid = True

        
        
        if(self.poids >= 500 and self.poids <= 2000 and self.poids % 500 == 0) : 
            pValid = True
        
        
        
        if (sum(self.compo_grains) == 100) :
            cValid = True 

        return tValid and pValid and cValid and gValid
    
        