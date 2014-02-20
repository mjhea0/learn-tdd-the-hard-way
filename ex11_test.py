import unittest
from ex11 import RawInput

class TestRawInput(unittest.TestCase):

    def setUp(self):
        age = raw_input()
        height = raw_input()
        weight = raw_input()
        self.create = RawInput(age,height,weight)

    def tearDown(self):
        pass

    def test_print_it(self):
        results = "How old are you? 10 How tall are you? 20 How much do you weigh? 30"
        self.assertEqual(self.create.print_it(),results)

if __name__ == '__main__':
    unittest.main()
