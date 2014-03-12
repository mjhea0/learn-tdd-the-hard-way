import os


class BranchesFunctions(object):

    def __init__(self, timid_bear):
        self.timid_bear = timid_bear

    def gold_room(self):
        next = raw_input("\nThis room is full of gold. \nHow much do you take? (round to the nearest 10) ")

        if "0" in next:
            how_much = int(next)
        else:
            return "\nMan, round to the neartest 10.\n"
        if how_much < 50:
            return "\nNice, you're not greedy, you win!\n"
        else:
            return "\nYou greedy bastard!\n"

    def bear_room(self):
        while True:
            next = raw_input("\nDo you take the 'honey' or 'taunt' the bear? ")
            output_list = []

            if next == "honey":
                return "\nThe bear looks at you then slaps your face off.\n"
            elif next == "taunt" and not self.timid_bear:
                output = "\nThe bear has moved from the door. You can go through it now."
                self.timid_bear = True
                open_door = True
                output_list.extend([output,open_door])
                return output_list
            elif next == "taunt" and self.timid_bear:
                return "\nThe bear gets pissed off and chews your leg off.\n"
            else:
                return "\nI got no idea what that means. Bye.\n"

    def cthulhu_room(self):
        start_over = True
        next_list = []
        next = raw_input("\nDo you 'flee' for your life or eat your 'head'? ")

        if "head" in next:
            return "Well that was tasty!"
        else:
            return start_over

    def start(self):
        which_room = raw_input("There is a door to your 'right' and 'left'. \nWhich one do you take? ")
        return which_room

    def cls(self):
        os.system(['clear','cls'][os.name == 'nt'])


if __name__ == '__main__':
    
    timid_bear = False
    create = BranchesFunctions(timid_bear)
    create.cls()
    print"#---------START!---------#"
    which_room = create.start()

    # bear room
    if which_room == "left":
        create.cls()
        print"#---------BEAR ROOM---------#"
        print "There is a bear here.\nThe bear has a bunch of honey. \
\nThe fat bear is in front of another door. \nHow are you going to move the bear?"
        results = create.bear_room()
        if type(results) == list:
            create.cls()
            print"#---------GOLD ROOM---------#"
            # gold room
            print create.gold_room()
        else: 
            print results
    # cthulhu room
    elif which_room == "right":
        create.cls()
        print"#---------CTHULHU ROOM---------#"
        print "Here you see the great evil Cthulhu. \nHe, it, whatever stares at you and you go insane."
        results = create.cthulhu_room()
        if results == True:
            # results = create.cthulhu_room()
        else:
            # which_room = create.start()
#     else:
#         print "You stumble around in the dark."
    
