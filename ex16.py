class ReadingWriting(object):

    def __init__(self, filename, target):
        self.filename = filename
        self.target = target

    def erase_file(self):
        return "We're going to erase {}".format(self.filename)

    def truncate_file(self):
        self.target.truncate()
        return "Truncating the file ..."

    def write_to_file(self):
        self.target.write(raw_input("line 1: "))
        self.target.write("\n")
        self.target.write(raw_input("line 2: "))
        self.target.write("\n")
        self.target.write(raw_input("line 3: "))
        self.target.write("\n")
        return "Writing to file ..."

    def close_file(self):
        self.target.close()
        return "Closing the file."

    def read_file(self):
        text = open(self.filename)
        return text.read()

# filename = "ex16_sample.txt"
# target = open(filename, 'w')


# test = ReadingWriting(filename, target)
# print test.erase_file()
# print test.truncate_file()
# print test.write_to_file()
# print test.close_file()
# print test.read_file()








