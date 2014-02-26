class Parameters(object):
    
    def __init__(self, script, first, second, third):
        self.script = script 
        self.first = first 
        self.second = second
        self.third = third

    def output(self):
        return "The script is called: {} \
Your first variable is: {} \
Your second variable is: {} \
Your third variable is: {}".format(self.script,self.first,self.second, self.third)
