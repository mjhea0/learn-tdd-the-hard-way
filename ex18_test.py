import unittest
from ex18 import Functions

class TestFunctions(unittest.TestCase):

    def setUp(self):
        arg1 = "test"
        arg2 = "test again"
        self.create = Functions(arg1, arg2)

    def tearDown(self):
        pass

    def test_print_two(self):
        self.assertEqual(self.create.print_two(), "arg1: test, arg2: test again")

    def test_print_two_again(self):
        self.assertEqual(self.create.print_two_again(), "arg1: test, arg2: test again")

    def test_print_one(self):
        self.assertEqual(self.create.print_one(), "arg1: test")

    def test_print_none(self):
        self.assertEqual(self.create.print_none(), "I got nothin'.")


if __name__ == '__main__':
    unittest.main()
