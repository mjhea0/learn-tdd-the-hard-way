class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            yield line

if __name__ == '__main__':
    happy_bday = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
    create = Song(happy_bday)
    for x in create.sing_me_a_song():
        print x
