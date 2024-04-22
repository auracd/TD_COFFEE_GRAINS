import unittest
from Sachet import Sachet
from Grain import Grain

class TestS(unittest.TestCase) : 
    def setUp(self) : 
        self.sachet1 = Sachet(500, "mixte", [Grain("Vietnam", "Floral", 2020, 6), Grain("Kenya", "Epice", 2022, 7)], [80, 20]); 
        self.sachet2 = Sachet(200, "grain",[Grain("Vietnam", "Floral", 2020, 6), Grain("Kenya", "Epice", 2022, 7)], [110, 34]);
        self.sachet3 = Sachet(2000, "pure",[Grain("Vietnam", "Floral", 2020, 6), Grain("Kenya", "Epice", 2022, 7)], [100]);

    def test_isGood(self) : 
        self.assertTrue(self.sachet1.is_valid())

    def test_isNotGood(self): 
        self.assertFalse(self.sachet2.is_valid())
        self.assertFalse(self.sachet3.is_valid())
  

    if __name__ == "__main__" : 
        unittest.main()

   

        