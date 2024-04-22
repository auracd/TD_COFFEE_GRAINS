import unittest
from Grain import Grain

class TestG(unittest.TestCase) : 
    def setUp(self) : 
        self.grain1 = Grain("France", "Fleur", 2005, 6); 
        self.grain2 = Grain("Vietnam", "Chocolate",2023, 8);

    def test_isGood(self) : 
        self.assertTrue(self.grain2.is_valid())

    def test_isNotGood(self): 
        self.assertFalse(self.grain1.is_valid())

    if __name__ == "__main__" : 
        unittest.main()

   

        