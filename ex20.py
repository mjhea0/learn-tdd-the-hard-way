class FunctionsFiles(object):

    def __init__(self, current_file):
        self.current_file = current_file

    def print_all(self):
        return "First let's print the whole file:\n{}".format(open(self.current_file).read())

    def rewind(self):
        output_list = []
        output_list.extend(["Now let's rewind, kind of like a tape.",
            (open(self.current_file, 'r').seek(0))])
        return output_list

    def print_a_line(self):
        out_list = []
        out_list.append("\nLet's print three lines:\n")
        for line in open(current_file,'r'):
            out_list.append(line)
        return out_list

current_file = "ex20_text.txt"

test = FunctionsFiles(current_file)
print test.print_all()
print test.rewind()[0]
print test.print_a_line()[0]
print test.print_a_line()[1]
print test.print_a_line()[2]
print test.print_a_line()[3]



