class LoopsLists(object):

    def __init__(self, the_count, fruits, change):
        self.the_count = the_count
        self.fruits = fruits
        self.change = change

    def number_loop(self):
        for number in self.the_count:
            print "This is count {}".format(number)

    def fruit_loop(self):
        for fruit in self.fruits:
            print "A fruit of type: {}".format(fruit)

    def mixed_loop(self):
        for i in self.change:
            print "I got {}".format(i)

    def range_loop(self):
        elements = []
        for i in range(0, 6):
            elements.append(i)
        for i in elements:
            print "Element was: {}".format(i)
