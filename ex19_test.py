import unittest
from ex19 import FunctionsVariables

class TestFunctionsVariables(unittest.TestCase):

    def setUp(self):
        self.create = FunctionsVariables(20,30)

    def tearDown(self):
        pass

    def test_call_cheese_and_crackers(self):
        self.assertEqual(self.create.call_cheese_and_crackers(),"You have 20 cheeses! You have 30 boxes of crackers! Man that's enough for a party! Get a blanket.\n")


if __name__ == '__main__':
    unittest.main()
