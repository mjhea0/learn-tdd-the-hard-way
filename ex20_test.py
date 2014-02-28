import unittest
from ex20 import FunctionsFiles

class TestFunctionsFiles(unittest.TestCase):

    def setUp(self):
        current_file = "ex20_text.txt"
        self.create = FunctionsFiles(current_file)

    def tearDown(self):
        pass

    def test_print_all(self):
        self.assertEqual(self.create.print_all(),"First let's print the whole file:\n\
This is line 1\nThis is line 2\nThis is line 3\n")

    def test_rewind(self):
        self.assertEqual(self.create.rewind(),["Now let's rewind, kind of like a tape.", None])

    def test_print_a_line(self):
        self.assertEqual(self.create.print_a_line(),["\nLet's print three lines:\n", 'This is line 1\n', \
            'This is line 2\n', 'This is line 3\n'])


if __name__ == '__main__':
    unittest.main()


