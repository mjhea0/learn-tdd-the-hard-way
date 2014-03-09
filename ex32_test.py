import unittest
from ex32 import LoopsLists

class TestLoopsLists(unittest.TestCase):

    def setUp(self):
        self.the_count = [1, 2, 3, 4, 5]
        self.fruits = ['apples', 'oranges', 'pears', 'apricots']
        self.change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

        self.create = LoopsLists(self.the_count,self.fruits,self.change)

    def tearDown(self):
        pass

    def test_number_loop(self):
        self.assertEqual(self.create.number_loop(),"test")

    def test_fruit_loop(self):
        self.assertEqual(self.create.fruit_loop(),"test")

    def test_mixed_loop(self):
        self.assertEqual(self.create.mixed_loop(),"test")

    def test_range_loop(self):
        self.assertEqual(self.create.range_loop(),"test")


if __name__ == '__main__':
    unittest.main()
