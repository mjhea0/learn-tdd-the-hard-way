
class BranchesFunctions(object):

    def __init__(self, which_room, timid_bear):
        self.which_room = which_room
        self.timid_bear = timid_bear

    def gold_room(self):
        next = raw_input("\nThis room is full of gold. How much do you take? (Round to the nearest 10) ")

        if "0" in next:
            how_much = int(next)
        else:
            return "Man, learn to type a number."

        if how_much < 50:
            return "Nice, you're not greedy, you win!"
        else:
            return "You greedy bastard!"

    def bear_room(self):
        while True:
            next = raw_input("Do you 'take honey' or 'taunt bear'? ")
            output_list = []

            if next == "take honey":
                output_list.append("\nThe bear looks at you then slaps your face off.")
            elif next == "taunt bear" and not self.timid_bear:
                output = "\nThe bear has moved from the door. You can go through it now."
                self.timid_bear = True
                open_door = True
                output_list.extend([output,open_door])
            elif next == "taunt bear" and self.timid_bear:
                output_list.append("\nThe bear gets pissed off and chews your leg off.")
            else:
                output_list.append("\nI got no idea what that means. Bye.")
            return output_list

    def cthulhu_room(self):
        start_over = False
        next_list = []
        next = raw_input("Do you 'flee' for your life or eat your 'head'? ")

        if "flee" in next:
            start_over = True
            next_list.append(start_over)
        elif "head" in next:
            next_list.extend([0,"Well that was tasty!"])
        else:
            next_list.append(start_over)
        return next_list


if __name__ == '__main__':
    which_room = raw_input("\nThere is a door to your 'right' and 'left'. Which one do you take? ")
    timid_bear = False
    create = BranchesFunctions(which_room, timid_bear)
    if which_room == "left":
        print "\nThere is a bear here. The bear has a bunch of honey. \
The fat bear is in front of another door. How are you going to move the bear?"
        results = create.bear_room()
        print results[0]
        if results[1]:
            print create.gold_room()
    elif which_room == "right":
        print "Here you see the great evil Cthulhu. He, it, whatever stares at you and you go insane."
        results = create.cthulhu_room()
        if results[0] == False:
            results = create.cthulhu_room()
        elif results[0] == True:
            which_room = raw_input("\nThere is a door to your 'right' and 'left'. Which one do you take? ")
        else:
            print results[1]
    else:
        print "You stumble around in the dark."
    
