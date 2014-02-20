class Prompting(object):
    
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def print_it(self):
        return "So, you're {} old, {} tall and {} heavy.".format(self.age, self.height, self.weight)
