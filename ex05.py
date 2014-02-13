class AboutMe(object):

    def __init__(self, my_name, my_age, my_height, my_weight, my_eyes, my_teeth, my_hair):
        self.my_name = my_name
        self.my_age = my_age
        self.my_height = my_height
        self.my_weight = my_weight
        self.my_eyes = my_eyes
        self.my_teeth = my_teeth
        self.my_hair = my_hair

    def output(self):
        return "Let's talk about {}. He's {} inches tall. He's {} pounds heavy." \
            " Actually that's not too heavy. He's got {} eyes and {} hair." \
            " His teeth are usually {} depending on the" \
            " coffee.".format(self.my_name, self.my_height, self.my_weight, self.my_eyes, self.my_hair, self.my_teeth)

    def add_age_weight_height(self):
        return "If I add {}, {}, and {}" \
        " I get {}.".format(self.my_age, self.my_height, self.my_weight, self.my_age + self.my_height + self.my_weight)
