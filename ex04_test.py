import unittest
from ex04 import CarsDrivers

class TestCarsDrivers(unittest.TestCase):

    def setUp(self):
        self.all_counts = CarsDrivers(100,4.0,30,90)

    def test_count_cars(self):
        self.assertEqual(self.all_counts.count_cars(), \
            "There are 100 cars available.")

    def test_count_drivers(self):
        self.assertEqual(self.all_counts.count_drivers(), \
            "There are only 30 drivers available.")

    def test_empty_cars(self):
        self.assertEqual(self.all_counts.count_empty_cars(), \
            "There will be 70 empty cars today.")

    def test_count_transports(self):
        self.assertEqual(self.all_counts.count_transports(), \
            "We can transport 120.0 people today.")

    def test_count_passengers(self):
        self.assertEqual(self.all_counts.count_passengers(), \
            "We have 90.0 to carpool today.") 

    def test_count_passengers_per_car(self):
        self.assertEqual(self.all_counts.count_passengers_per_car(), \
            "We need to put about 3.0 in each car.")


if __name__ == '__main__':
    unittest.main()
