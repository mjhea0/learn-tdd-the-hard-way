class MorePrinting(object):

    def __init__(self, days, months):
        self.days = days
        self.months = months

    def print_it(self):
        return "Here are the days: {} \
Here are the months:  {} \
There's something going on here. \
With the three double-quotes. \
We'll be able to type as much as we like. \
Even 4 lines if we want, or 5, or 6.".format(self.days,self.months)



