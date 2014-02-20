import unittest
from ex10 import BackSlash

class TestBackslash(unittest.TestCase):

    def setUp(self):
        tabby_cat = "\tI'm tabbed in."
        persian_cat = "I'm split\non a line."
        backslash_cat = "I'm \\ a \\ cat."
        fat_cat = """
        I'll do a list:
        \t* Cat food
        \t* Fishies
        \t* Catnip\n\t* Grass
        """
        self.create = BackSlash(tabby_cat,persian_cat,backslash_cat,fat_cat)

    def tearDown(self):
        pass

    def test_print_it(self):
        results = "\tI'm tabbed in. I'm split\non a line. I'm \\ a \\ cat. \n        I'll do a list:\n        \t* Cat food\n        \t* Fishies\n        \t* Catnip\n\t* Grass\n        "
        self.assertEqual(self.create.print_it(),results)


if __name__ == '__main__':
    unittest.main()
