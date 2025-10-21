import unittest
from addNumbers import add_numbers


class TestPositive(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

class TestNegative(unittest.TestCase):

    def test_add_negative_numbers(self):
        result = add_numbers(-1, -4)
        self.assertEqual(result, -5)


if __name__ == '__main__':
    unittest.main()