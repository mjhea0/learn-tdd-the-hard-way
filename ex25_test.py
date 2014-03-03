import unittest
from ex25 import MorePractice

class TestMorePractice(unittest.TestCase):

    def setUp(self):
        sentence = "All good things come to those who wait."
        self.create = MorePractice(sentence)

    def tearDown(self):
        pass

    def test_break_words(self):
        sentence = "All good things come to those who wait."
        self.assertEqual(self.create.break_words(sentence), 
            ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.'])

    def test_sort_words(self):
        words = ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
        self.assertEqual(self.create.sort_words(words), 
            ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who'])

    def test_print_first_word(self):
        words = ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
        self.assertEqual(self.create.print_first_word(words), "All")

    def test_print_last_word(self):
        words = ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
        self.assertEqual(self.create.print_last_word(words), "wait.")


if __name__ == '__main__':
    unittest.main()



