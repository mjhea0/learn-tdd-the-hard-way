import unittest
from ex25 import MorePractice

class TestMorePractice(unittest.TestCase):

    def setUp(self):
        self.sentence = "All good things come to those who wait."
        self.words = self.sentence.split(' ')
        self.create = MorePractice(self.sentence)

    def tearDown(self):
        pass

    def test_break_words(self):
        self.assertEqual(self.create.break_words(self.sentence), 
            ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.'])

    def test_sort_words(self):
        self.assertEqual(self.create.sort_words(self.words), 
            ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who'])

    def test_print_first_word(self):
        self.assertEqual(self.create.print_first_word(self.words), "All")

    def test_print_last_word(self):
        self.assertEqual(self.create.print_last_word(self.words), "wait.")


if __name__ == '__main__':
    unittest.main()



