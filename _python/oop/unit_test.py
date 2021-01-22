# import the python testing framework
import unittest


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# initialized by creating a class that inherits from unittest.TestCase


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        self.assertTrue(isEven(2))

    def testThree(self):
        self.assertEqual(isEven(3), False)
        self.assertFalse(isEven(3))

    def setUp(self):
        print("running setup")

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()
