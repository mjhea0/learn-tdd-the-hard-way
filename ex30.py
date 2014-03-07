class ElseIf(object):

    def __init__(self, people, cars, buses):
        self.people = people
        self.cars = cars
        self.buses = buses

    def first_else(self):
        if self.cars > self.people:
            return "We should take the cars."
        elif self.cars < self.people:
            return "We should not take the cars."
        else:
            return "We can't decide."

    def second_else(self):
        if self.buses > self.cars:
            return "That's too many buses."
        elif self.buses < self.cars:
            return "Maybe we could take the buses."
        else:
            return "We still can't decide."

    def third_else(self):
        if self.people > self.buses:
            return "Alright, let's just take the buses."
        else:
            return "Fine, let's stay home then."


if __name__ == '__main__':
    create = ElseIf(30,40,15)
    print create.first_else()
    print create.second_else()
    print create.third_else()
