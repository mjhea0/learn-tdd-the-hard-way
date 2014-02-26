import unittest
from ex14 import Prompt

class TestPrompt(unittest.TestCase):

    def setUp(self):
        self.create = Prompt("test","test","test","test","test")

    def tearDown(self):
        pass

    def test_output_script(self):
        self.assertEqual(self.create.output_script(), "Hi test, I'm the test script. I'd like to ask you a few questions. Do you like me test?")

    def test_output_main(self):
        self.assertEqual(self.create.output_main(), "Alright, so you said test about liking me. You live in test.  Not sure where that is. And you have a test computer.  Nice.")


if __name__ == '__main__':
    unittest.main()
