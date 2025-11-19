"""Unit tests for the project."""
import unittest
from add_numbers import add_numbers

class TestPositive(unittest.TestCase):
    """Test cases for adding positive numbers."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers returns correct sum."""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

class TestNegative(unittest.TestCase):
    """Test cases for adding negative numbers."""

    def test_add_negative_numbers(self):
        """Test adding two negative numbers returns correct sum."""
        result = add_numbers(-1, -4)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()
