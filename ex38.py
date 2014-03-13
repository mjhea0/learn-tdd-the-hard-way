class ListManipulation(object):

    def __init__(self, ten_things, more_stuff):
        self.ten_things = ten_things
        self.more_stuff = more_stuff

    def output_list(self):
        return self.ten_things

    def add_to_list(self):
        stuff = self.ten_things.split(' ')
        while len(stuff) != 10:
            next_one = self.more_stuff.pop()
            stuff.append(next_one)
        return stuff
            

if __name__ == '__main__':
    ten_things = "Apples Oranges Crows Telephone Light Sugar"
    more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
    create = ListManipulation(ten_things, more_stuff)

    print "\nCurrent list: {}".format(create.output_list())
    print "Wait there's not 10 things in that list, let's fix that."
    stuff = create.add_to_list()
    print "There's {} items now:".format(len(stuff))
    print "New list: {}\n".format(stuff)
