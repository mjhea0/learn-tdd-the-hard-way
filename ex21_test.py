import unittest
from ex21 import FunctionReturns

class TestFunctionReturns(unittest.TestCase):

    def setUp(self):
        self.create = FunctionReturns()

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self.create.add(30, 5), 35)

    def test_subtract(self):
        self.assertEqual(self.create.subtract(78, 4), 74)

    def test_multiply(self):
        self.assertEqual(self.create.multiply(90, 2), 180)

    def test_divide(self):
        self.assertEqual(self.create.divide(100, 2), 50)


if __name__ == '__main__':
    unittest.main()

