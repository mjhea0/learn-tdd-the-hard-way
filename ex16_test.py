import unittest
from ex16 import ReadingWriting

class TestReadingWriting(unittest.TestCase):

    def setUp(self):
        filename = "ex16_sample.txt"
        target = open(filename, 'w')
        self.create = ReadingWriting(filename, target)

    def tearDown(self):
        pass

    def test_1_erase_file(self):
        self.create.erase_file()
        text = open("ex16_sample.txt")
        self.assertEqual(text.read(), '')

    def test_2_read_file(self):
        self.create.write_to_file()
        self.create.close_file()
        self.assertEqual(self.create.read_file(), "t\nt\nt\n")

if __name__ == '__main__':
    unittest.main()
