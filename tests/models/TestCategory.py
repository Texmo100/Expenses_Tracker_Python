import unittest
from unittest import TestCase
from unittest.mock import patch
from src.expenses_tracker.models.Category import Category
from io import StringIO

class TestCategory(TestCase):
    def setUp(self):
        self.obj = Category("games", "this is a very large description to demonstrate it works", 1000.00)
    
    def tearDown(self):
        self.obj = None

    def test_category_initialization(self):
        self.assertIsInstance(self.obj, Category)
        self.assertEqual(self.obj.name, "games")
        self.assertEqual(self.obj.description, "this is a very large description to demonstrate it works")
        self.assertEqual(self.obj.limit, 1000.00)

    def test_category_setters_with_valid_values(self):
        self.obj.name = "house"
        self.obj.description = "this is another large text"
        self.obj.limit = 5000.00

        self.assertEqual(self.obj.name, "house")
        self.assertEqual(self.obj.description, "this is another large text")
        self.assertEqual(self.obj.limit, 5000.00)

    @patch("sys.stdout", new_callable=StringIO)
    def test_category_setters_with_invalid_values(self, mock_stdout):
        self.obj.name = "*&*^%$^^*"
        self.obj.description = "789318713HUUH"
        self.obj.limit = 0

        errors_caught = mock_stdout.getvalue().split("\n")

        self.assertIn("Not a valid value for name", errors_caught)
        self.assertIn("Not a valid value for description", errors_caught)
        self.assertIn("Not a valid value for limit", errors_caught)

        self.assertNotEqual(self.obj.name, "*&*^%$^^*")
        self.assertNotEqual(self.obj.description, "word")
        self.assertNotEqual(self.obj.limit, 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_category_show_short_info(self, mock_stdout):
        self.obj.show_short_info()

        messages_caught = mock_stdout.getvalue().split("\n")

        self.assertIn(f'{self.obj.id}: {self.obj.name}', messages_caught)
    
    @patch("sys.stdout", new_callable=StringIO)
    def test_category_show_detailed_info(self, mock_stdout):
        self.obj.show_detailed_info()

        messages_caught = mock_stdout.getvalue().split("\n")

        self.assertIn(f'ID: {self.obj.id}', messages_caught)
        self.assertIn(f'Name: {self.obj.name}', messages_caught)
        self.assertIn(f'Description: {self.obj.description}', messages_caught)
        self.assertIn(f'Budget Limit: {self.obj.limit}', messages_caught)

if __name__ == "__main__":
    unittest.main()
