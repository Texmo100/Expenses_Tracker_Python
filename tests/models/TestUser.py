import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.models.User import User

class TestUser(TestCase):
    def setUp(self):
        self.obj = User("isaac", "iniguez", "6645209011", "lagos de peru")
    
    def tearDown(self):
        self.obj = None

    def test_user_initialization(self):
        self.assertEqual(self.obj.firstname, "isaac")
        self.assertEqual(self.obj.lastname, "iniguez")
        self.assertEqual(self.obj.phone_number, "6645209011")
        self.assertEqual(self.obj.address, "lagos de peru")

    def test_user_setters_with_valid_values(self):
        self.obj.firstname = "ariel"
        self.obj.lastname = "perez"
        self.obj.phone_number = "6678902345"
        self.obj.address = "santa rosalia"

        self.assertEqual(self.obj.firstname, "ariel")
        self.assertEqual(self.obj.lastname, "perez")
        self.assertEqual(self.obj.phone_number, "6678902345")
        self.assertEqual(self.obj.address, "santa rosalia")
    
    @patch("sys.stdout", new_callable=StringIO)
    def test_user_setters_with_invalid_values(self, mock_stdout):
        self.obj.firstname = "8971238972 317893128972"
        self.obj.lastname = "8108931280923 890123890312"
        self.obj.phone_number = "home"
        self.obj.address = "&*((*&8hu7u98731))"

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Not a valid value for firstname", error_messages)
        self.assertIn("Not a valid value for lastname", error_messages)
        self.assertIn("Not a valid value for phone_number", error_messages)
        self.assertIn("Not a valid value for address", error_messages)

if __name__ == "__main__":
    unittest.main()
