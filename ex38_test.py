import unittest
from ex38 import ListManipulation

class TestListManipulation(unittest.TestCase):

    def setUp(self):
        ten_things = "Apples Oranges Crows Telephone Light Sugar"
        more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
        self.create = ListManipulation(ten_things, more_stuff)

    def tearDown(self):
        pass

    def test_output_list(self):
        self.assertEqual(self.create.output_list(),"Apples Oranges Crows Telephone Light Sugar")

    def test_add_to_list(self):
        self.assertEqual(self.create.add_to_list(),['Apples', 'Oranges', 'Crows', 
            'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn'])


if __name__ == '__main__':
    unittest.main()
