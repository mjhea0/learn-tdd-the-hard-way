class FunctionsVariables(object):

    def __init__(self, cheese_count, boxes_of_crackers):
        self.cheese_count = cheese_count
        self.boxes_of_crackers = boxes_of_crackers

    def call_cheese_and_crackers(self):
        return "You have {} cheeses! \
You have {} boxes of crackers! \
Man that's enough for a party! \
Get a blanket.\n".format(self.cheese_count, self.boxes_of_crackers)
