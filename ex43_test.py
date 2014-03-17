import unittest
from ex43 import Scene

class TestEngine(unittest.TestCase):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



if __name__ == '__main__':
    unittest.main()


    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()
