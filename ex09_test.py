import unittest
from ex09 import MorePrinting

class TestMorePrinting(unittest.TestCase):

    def setUp(self):
        days = "Mon Tue Wed Thu Fri Sat Sun"
        months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
        self.output = MorePrinting(days,months)

    def tearDown(self):
        pass

    def test_print_it(self):
        results = "Here are the days: Mon Tue Wed Thu Fri Sat Sun Here are the months:  Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug There's something going on here. With the three double-quotes. We'll be able to type as much as we like. Even 4 lines if we want, or 5, or 6."
        self.assertEqual(self.output.print_it(),results)

if __name__ == '__main__':
    unittest.main()
