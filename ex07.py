class LittleLamb(object):

    def __init__(self,fleece_metaphor,num):
        self.fleece_metaphor = fleece_metaphor
        self.num = num

    def print_output(self):
        return "Mary had a little lamb. \
Its fleece was white as {}.\
 And everywhere that Mary went. \
{} \
Cheese Burger".format(self.fleece_metaphor, self.num * ".")
