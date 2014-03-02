class FunctionReturns(object):

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def output(self,age,height,weight,iq):
        return "Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq)

if __name__ == '__main__':
    print "Let's do some math with just functions!"
    test = FunctionReturns()
    age = test.add(30, 5)
    height = test.subtract(78, 4)
    weight = test.multiply(90, 2)
    iq = test.divide(100, 2)
    print test.output(age,height,weight,iq)
