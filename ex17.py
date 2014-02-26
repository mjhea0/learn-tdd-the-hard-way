class MoreFiles(object):

    def __init__(self, from_file, to_file, from_file_data):
        self.from_file = from_file
        self.to_file = to_file
        self.from_file_data = from_file_data

    def copy_files(self):
        out_file = open(self.to_file, 'w')
        out_file.write(self.from_file_data)
        return "The input file is {} bytes long. \
Copying from {} to {}".format(len(from_file_data), self.from_file, self.to_file)

    def read_file(self):
        return open(self.to_file).read()


# from_file = "test.txt"
# to_file = "ex17_sample.txt"
# from_file_data = open(from_file).read()

# test = MoreFiles(from_file, to_file, from_file_data)
# print test.copy_files()
# print test.read_file()









