import unittest
from ex15 import ReadingFiles

class TestReadingFiles(unittest.TestCase):

    def setUp(self):
        filename = "ex15_sample.txt"
        self.create = ReadingFiles(filename)

    def tearDown(self):
        pass

    def test_read_file(self):
        self.assertEqual(self.create.read_file(), "This is stuff I typed into a file.\nIt is really cool stuff.\nLots and lots of fun to have in here.\n")

if __name__ == '__main__':
    unittest.main()
