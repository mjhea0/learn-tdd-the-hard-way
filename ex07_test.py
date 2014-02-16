import unittest
from ex07 import LittleLamb

class TestLittleLamb(unittest.TestCase):

    def setUp(self):
        self.mary = LittleLamb("snow",10)


    def tearDown(self):
        pass

    def test_output(self):
        results = "Mary had a little lamb. Its fleece was white as snow.\
 And everywhere that Mary went. .......... Cheese Burger"
        self.assertEqual(self.mary.print_output(), results)


if __name__ == '__main__':
    unittest.main()
