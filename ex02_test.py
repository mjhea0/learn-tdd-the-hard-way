import unittest
from ex02 import Characters

class CharacterTest(unittest.TestCase):

    def setUp(self):
        self.printy = Characters()

    def test_comment_output(self):
        self.assertEqual(self.printy.output_comments(),None)

    def test_string_output(self):
        self.assertEqual(self.printy.output_strings("Hello World!"),"Hello World!")


if __name__ == '__main__':
    unittest.main()
