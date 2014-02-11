import unittest
from ex01 import String

class TestHelloWorld(unittest.TestCase):

    def test_function_can_print(self):
        self.printy = String()
        self.assertEqual(self.printy.print_string("Hello World!"),"Hello World!")
        self.assertEqual(self.printy.print_string("test"),"test")
        

if __name__ == '__main__':
    unittest.main()
