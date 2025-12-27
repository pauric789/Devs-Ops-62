"""Unit tests for the project."""
import unittest
from fastapi.testclient import TestClient
from add_numbers import add_numbers,app

client = TestClient(app)

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

class TestAPI(unittest.TestCase):
    """Test cases for the FastAPI endpoints."""

    def test_api_add_endpoint(self):
        """Test the /add web route returns JSON with the correct sum."""
        response = client.get("/add?a=10&b=20")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sum": 30})

if __name__ == '__main__':
    unittest.main()
