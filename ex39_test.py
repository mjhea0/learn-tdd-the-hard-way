import unittest
from ex39 import LovelyDictionaries

class TestLovelyDictionaries(unittest.TestCase):

    def setUp(self):
        # create a mapping of state to abbreviation
        states = {
            'Oregon': 'OR',
            'Florida': 'FL',
            'California': 'CA',
            'New York': 'NY',
            'Michigan': 'MI'
            }

        # create a basic set of states and some cities in them
        cities = {
            'CA': 'San Francisco',
            'MI': 'Detroit',
            'FL': 'Jacksonville'
        }
        self.create = LovelyDictionaries(states, cities)

    def tearDown(self):
        pass

    def test_add_cities(self):
        self.assertEqual(self.create.add_cities(),
            {'FL': 'Jacksonville', 'CA': 'San Francisco', 'MI': 'Detroit', 'OR': 'Portland', 'NY': 'New York'})



if __name__ == '__main__':
    unittest.main()
