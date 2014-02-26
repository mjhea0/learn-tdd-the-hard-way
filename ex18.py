class Functions(object):

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


    def print_two(self):
        return "arg1: {}, arg2: {}".format(self.arg1, self.arg2)

    def print_two_again(self):
        return "arg1: {}, arg2: {}".format(self.arg1, self.arg2)

    def print_one(self):
        return "arg1: {}".format(self.arg1)

    def print_none(self):
        return "I got nothin'."


# arg1 = "test"
# arg2 = "test again"

# test = Functions(arg1, arg2)
# print test.print_two()
# print test.print_two_again()
# print test.print_one()
# print test.print_none()
