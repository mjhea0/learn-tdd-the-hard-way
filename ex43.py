from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This is the function executed when entering a new room. Subsclasses should override it."
        print "Unless the player has ended the game, this function should return a string of the next scene to enter."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    
    orbituaries = [
        "The greatest programmer ever known has died today.",
        "Our hero is dead. The Gothons have one."
    ]

    def enter(self):
        print self.orbituaries[randint(0, len(self.orbituaries)-1)]
        exit(1)

class CentralCorridor(Scene):
    "This is the starting point and has a Gothon already standing there they have to defeat with a joke before continuing."

    def enter(self):
        print "A Gothon jumps out at you and is about to shoot. What do you do? [shoot!, dodge!, tell a joke]"
        while True:
            action = raw_input('> ')
            if action == "shoot!":
                print "You are still too slow because you haven't had coffee since you work up from cryosleep!"
                return 'death'
            elif action == "dodge!":
                print "You are too slow in this gravity!"
                return 'death'
            elif action == "tell a joke":
                return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):
    "This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad he has to guess the number for."

    def enter(self):
        print "You find an armory but the laser weapons are kept in a safe with a 3 digit code."
        attempts = 0
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "code = ", code
        while True:
            guess = raw_input('[keypad]> ')
            if guess == code:
                print "Correct!"
                return 'the_bridge'
            else:
                print "Incorrect!"
                attempts += 1
            if attempts == 3:
                print "Too many attempts!"
                return 'death'

class TheBridge(Scene):
    "Another battle scene with a Gothon where the hero places the bomb."    

    def enter(self):
        print "On the bridge are Gothons. What do you do with the bomb? [shoot, throw, place]"
        action = raw_input('> ')
        if action == "shoot":
            print "The bomb goes off."
            return 'death'
        elif action == "throw":
            print "You arm and throw the bomb and run but it goes off before you can reach the escape pod."
            return 'death'
        elif action == "place":
            print "You hold a gun to the bomb while you slowly make for the escape pods. Before leaving the bridge to place the bomb on the door."
            return 'escape_pod'
        else:
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print "Where the hero escapes but only after guessing the right escape pod."    
        code = randint(1,9)
        attempt = 0
        print "The escape pod is protected by single digit (1-9) code with 3 attempts."
        while attempt < 3:
            guess = int(raw_input('> '))
            if code == guess:
                print "Our hero escapes to the planet below and the Gothan ship explodes."
                exit(0)
            else:
                print "Code invalid! Try again."
                attempt += 1
        print "Too late, the bomb you placed on the bridge has detonated."
        return 'death'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        # return Map.scenes.get(scene_name)
        # more consistent alternative
        return self.scenes[scene_name]

    def opening_scene(self):
        # reuse the existing function to lookup scene
        return self.next_scene(self.start_scene)


if __name__ == '__main__':
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
