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
        #pour prendre en compte 1 et 9 dans les bornes 
        if (self.corps in range(0, 10)): 
            cVerif = True

        return oVerif and aVerif and rVerif and cVerif