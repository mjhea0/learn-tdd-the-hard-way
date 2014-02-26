import unittest
from ex17 import MoreFiles

class TestMoreFiles(unittest.TestCase):

    def setUp(self):
        from_file = "test.txt"
        to_file = "ex17_sample.txt"
        from_file_data = open(from_file).read()
        self.create = MoreFiles(from_file, to_file, from_file_data)

    def tearDown(self):
        pass


    def test_read_file(self):
        self.assertEqual(self.create.read_file(), "This is a test file.\n")



if __name__ == '__main__':
    unittest.main()
