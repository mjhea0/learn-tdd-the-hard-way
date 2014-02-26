import unittest
from ex13 import Parameters
from sys import argv

class TestParameters(unittest.TestCase):

    def setUp(self):
        self.create = Parameters(1,2,3,4)

    def tearDown(self):
        pass

    def test_output(self):
        self.assertEqual(self.create.output(),"The script is called: 1 Your first variable is: 2 Your second variable is: 3 Your third variable is: 4")

if __name__ == '__main__':
    unittest.main()
