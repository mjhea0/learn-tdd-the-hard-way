class ReadingFiles(object):

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        text = open(self.filename)
        return text.read()


# test = ReadingFiles("ex15_sample.txt")
# print test.read_file()
