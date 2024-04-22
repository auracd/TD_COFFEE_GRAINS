class Grain() : 
    def __init__(self, origin, arome, recolte, corps):
        self.origine = origin
        self.arome = arome
        self.recolte = recolte
        self.corps = corps


    def is_valid(self) : 
        o = ["Vietnam", "Kenya", "Colombie", "Guatemala"] 
        a = ["Floral", "Fruite", "Chocolate", "Epice"]
        
        oVerif = self.origine in o
        aVerif = self.arome in a 
        rVerif = False
        if (isinstance(self.recolte, int) and (self.recolte%5 != 0)) : 
            rVerif = True
        cVerif = False 
        if (self.corps in range.choice(range(1, 9))): 
            cVerif = True

        return oVerif and aVerif and rVerif and cVerif