class Printing(object):

    def __init__(self, integer_list, number_list, boolean_list):
        self.integer_list = integer_list
        self.number_list = number_list
        self.boolean_list = boolean_list

    def output(self):
        return "{} {} {} I had this thing.' 'That you could type up right.' 'But it didn't sing.' 'So I said goodnight.".format(
            (', '.join(str(x) for x in self.number_list)), 
            (', '.join(self.number_list)), 
            (', '.join(str(x) for x in self.boolean_list))
            )
