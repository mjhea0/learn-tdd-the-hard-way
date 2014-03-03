class MorePractice(object):

    def __init__(self, sentence):
        self.sentence = sentence

    def break_words(self, stuff):
        """This function will break up words for us."""
        words = stuff.split(' ')
        return words

    def sort_words(self, words):
        """Sorts the words."""
        return sorted(words)

    def print_first_word(self, words):
        """Prints the first word after popping it off."""
        word = words.pop(0)
        return word

    def print_last_word(self, words):
        """Prints the last word after popping it off."""
        word = words.pop(-1)
        return word



if __name__ == '__main__':
    sentence = "All good things come to those who wait."
    create = MorePractice(sentence)

    words = create.break_words(sentence)
    print words

    sorted_words = create.sort_words(words)
    print sorted_words

    print create.print_first_word(words)
    print create.print_last_word(words)
    print create.print_first_word(sorted_words)
    print create.print_last_word(sorted_words)

    print sorted_words

