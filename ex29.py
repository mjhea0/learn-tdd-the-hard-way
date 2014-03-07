class WhatIf(object):

    def __init__(self, people, cats, dogs):
        self.people = people
        self.cats = cats
        self.dogs = dogs

    def output_cats(self):
        if self.people < self.cats:
            return "Too many cats! The world is doomed!"
        elif self.people > self.cats:
            return "Not many cats! The world is saved!"

    def output_dogs(self):
        if self.people < self.dogs:
            return "The world is drooled on!"
        elif self.people > self.dogs:
            return "The world is dry!"


if __name__ == '__main__':
    create = WhatIf(10,5,7)
    print create.output_cats()
    print create.output_dogs()
