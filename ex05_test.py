import unittest
from ex05 import AboutMe

class TestAboutMe(unittest.TestCase):

    def setUp(self):
        self.all_attributes = AboutMe("Michael", 31, 70, 165, "blue", "white", "red")

    def test_about(self):
        self.assertEqual(self.all_attributes.output(), \
            "Let's talk about Michael. He's 70 inches tall." +
            " He's 165 pounds heavy. Actually that's not too heavy." +
            " He's got blue eyes and red hair. His teeth are usually white depending on the coffee.")

    def test_count_drivers(self):
        self.assertEqual(self.all_attributes.add_age_weight_height(), \
            "If I add 31, 70, and 165 I get 266.")


if __name__ == '__main__':
    unittest.main()
