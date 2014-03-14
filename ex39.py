class LovelyDictionaries(object):

    def __init__(self, states, cities):
        self.states = states
        self.cities = cities

    def add_cities(self):
        # add some more cities
        self.cities['NY'] = 'New York'
        self.cities['OR'] = 'Portland'
        return self.cities

if __name__ == '__main__':
    # create a mapping of state to abbreviation
    states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
    }

    # create a basic set of states and some cities in them
    cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
    }
    create = LovelyDictionaries(states, cities)
    cities = create.add_cities()


    # print out some cities
    print '-' * 10
    print "NY State has: {}".format(cities['NY'])
    print "OR State has: {}".format(cities['OR'])

    # print some states
    print '-' * 10
    print "Michigan's abbreviation is: {}".format(states['Michigan'])
    print "Florida's abbreviation is: {}".format(states['Florida'])
