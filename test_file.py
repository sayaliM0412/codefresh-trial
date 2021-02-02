import unittest
import helloworld

class test_suite(unittest.TestCase):
    def test_helloworld(self):
        o = helloworld.MyClass()
        val=o.HelloWorld()
        self.assertEqual("Hello World", val)


if __name__ == '__main__':
    unittest.main()