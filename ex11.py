class RawInput(object):

    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def print_it(self):
        return "How old are you? {} \
How tall are you? {} \
How much do you weigh? {}".format(self.age, self.height, self.weight)

