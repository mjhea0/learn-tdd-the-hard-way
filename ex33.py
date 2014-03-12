class WhileLoops(object):

    def __init__(self, i):
        self.i = i

    def loop(self):
        numbers = []
        while self.i < 6:
            numbers.append(self.i)
            self.i += 1
        return numbers


if __name__ == '__main__':
    create = WhileLoops(0)
    numbers = create.loop()
    print "The numbers are: {}".format(str(numbers).strip('[]'))
