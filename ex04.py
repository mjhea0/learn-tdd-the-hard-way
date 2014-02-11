class CarsDrivers(object):

    def __init__(self, cars, space_in_a_car, drivers, passengers):
        self.cars = cars
        self.space_in_a_car = space_in_a_car
        self.drivers = drivers
        self.passengers = passengers

    def count_cars(self):
        return "There are {} cars available.".format(self.cars)

    def count_drivers(self):
        return "There are only {} drivers available.".format(self.drivers)

    def count_transports(self):
        return "We can transport {} people today.".format(self.drivers*self.space_in_a_car)

    def count_empty_cars(self):
        return "There will be {} empty cars today.".format(self.cars-self.drivers)

    def count_passengers(self):
        return "We have {} to carpool today.".format((self.space_in_a_car-1)*self.drivers)

    def count_passengers_per_car(self):
        return "We need to put about {} in each car.".format(self.space_in_a_car-1)
