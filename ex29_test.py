import unittest
from ex29 import WhatIf

class TestWhatIf(unittest.TestCase):

    def setUp(self):
        self.create = WhatIf(10,5,7)

    def tearDown(self):
        pass

    def test_output_cats(self):
        self.assertEqual(self.create.output_cats(), "Not many cats! The world is saved!")

    def test_output_dogs(self):
        self.assertEqual(self.create.output_dogs(), "The world is dry!")

if __name__ == '__main__':
    unittest.main()
