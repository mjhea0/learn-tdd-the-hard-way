class AboutPeople(object):

    def __init__(self, num_people, num_people_again, is_funny):
        self.num_people = num_people
        self.num_people_again = num_people_again
        self.is_funny = is_funny

    def output(self):
        return "There are {} types of people. \
Those who know binary and those who don't. \
I said: 'There are {} types of people.'. \
I also said: 'Those who know binary and those who don't.'. \
Isn't that joke so funny?! {} \
This is the left side of...a string with a right side.".format(self.num_people, self.num_people_again, self.is_funny)


test = AboutPeople(10, 10, "False")
print test.output()

