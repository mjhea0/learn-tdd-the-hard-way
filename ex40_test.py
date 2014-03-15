import unittest
from ex40 import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        happy_bday = ["\nHappy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
        self.create = Song(happy_bday)
        for self.x in self.create.sing_me_a_song():
            return self.x

    def tearDown(self):
        pass

    def test_sing_me_a_song(self):
        self.assertEqual(self.x,"\nHappy birthday to you")

if __name__ == '__main__':
    unittest.main()
