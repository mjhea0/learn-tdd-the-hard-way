import unittest
from ex33 import WhileLoops

class TestWhileLoops(unittest.TestCase):

    def setUp(self):
        self.create = WhileLoops(0)

    def tearDown(Self):
        pass

    def test_loop(self):
        self.assertEqual(self.create.loop(),[0, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
