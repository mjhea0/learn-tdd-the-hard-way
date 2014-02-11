import unittest
from ex03 import Chickens

class CountChickensEggss(unittest.TestCase):

    def setUp(self):
        self.animal = Chickens()

    def test_count_chickens(self):
        self.assertEqual(self.animal.count_hens(),"Hens: 30")

    def test_count_roosters(self):
        self.assertEqual(self.animal.count_roosters(),"Roosters: 97")

    def test_count_eggs(self):
        self.assertEqual(self.animal.count_eggs(),"Eggs: 7")


if __name__ == '__main__':
    unittest.main()
