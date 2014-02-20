import unittest
from ex12 import Prompting

class TestPrompting(unittest.TestCase):
    
    def setUp(self):
        age = raw_input("How old are you? ")
        height = raw_input("How tall are you? ")
        weight = raw_input("How much do you weigh? ")
        self.create = Prompting(age,height,weight)

    def tearDown(self):
        pass

    def test_print_it(self):
        results = "So, you're 10 old, 20 tall and 30 heavy."
        self.assertEqual(self.create.print_it(),results)



if __name__ == '__main__':
    unittest.main()
