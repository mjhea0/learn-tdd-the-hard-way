import unittest
from ex30 import ElseIf

class TestElseIf(unittest.TestCase):

    def setUp(self):
        self.create = ElseIf(30,40,15)

    def tearDown(self):
        pass

    def test_first_else(self):
        self.assertEqual(self.create.first_else(), "We should take the cars.")

    def test_second_else(self):
        self.assertEqual(self.create.second_else(), "Maybe we could take the buses.")

    def test_third_else(self):
        self.assertEqual(self.create.third_else(), "Alright, let's just take the buses.")


if __name__ == '__main__':
    unittest.main()
