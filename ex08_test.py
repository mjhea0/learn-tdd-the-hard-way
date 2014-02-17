import unittest
from ex08 import Printing


class TestPrinting(unittest.TestCase):

    def setUp(self):
        self.results = Printing(["1","2","3","4"],["One", "Two", "Three", "Four"], [True,False,False,True])

    def tearDown(self):
        pass

    def test_output(self):
        result = "One, Two, Three, Four One, Two, Three, Four True, False, False, True I had this thing.' 'That you could type up right.' 'But it didn't sing.' 'So I said goodnight."
        self.assertEqual(self.results.output(), result)


if __name__ == '__main__':
    unittest.main()
