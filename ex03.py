class Chickens(object):

    def count_hens(self):
        return "Hens: {}".format(25+30/6)

    def count_roosters(self):
        return "Roosters: {}".format(100-25*3%4)

    def count_eggs(self):
        return "Eggs: {}".format(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
