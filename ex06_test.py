import unittest
from ex06 import AboutPeople

class TestAboutPeople(unittest.TestCase):

    def setUp(self):
        self.all_attributes = AboutPeople(10, 10, "False")

    def test_about(self):
        self.assertEqual(self.all_attributes.output(), \
            "There are 10 types of people. Those who know" + 
            " binary and those who don't. I said: 'There" +
            " are 10 types of people.'. I also said:" +
            " 'Those who know binary and those who don't.'." 
            " Isn't that joke so funny?! False This is the" +
            " left side of...a string with a right side.")


if __name__ == '__main__':
    unittest.main()
