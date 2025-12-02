from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from datetime import date
from src.expenses_tracker.models.Budget import Budget
from src.expenses_tracker.models.Category import Category

class TestBudget(TestCase):
    def setUp(self):
        test_category = Category()
        self.obj = Budget("work", test_category, (100.00, 1000.00))

    def tearDown(self):
        self.obj = None

    def test_budget_initialization(self):
        self.assertIsInstance(self.obj, Budget)
        self.assertEqual(self.obj.name, "work")
        self.assertIsInstance(self.obj.category, Category)
        self.assertEqual(self.obj.b_range, (100.00, 1000.00))
        self.assertEqual(self.obj.created_at, date.today())

    def test_budget_setters_with_valid_values(self):
        self.obj.name = "school"
        self.obj.category = Category()
        self.obj.b_range = (50.00, 100.00)

        self.assertEqual(self.obj.name, "school")
        self.assertIsInstance(self.obj.category, Category)
        self.assertEqual(self.obj.b_range, (50.00, 100.00))

    @patch("sys.stdout", new_callable=StringIO)
    def test_budget_setters_with_invalid_values(self, mock_stdout):
        self.obj.name = "^&*&$%^"
        self.obj.category = Budget()
        self.obj.b_range = 1000

        errors_caught = mock_stdout.getvalue().split("\n")

        self.assertIn("Not a valid value for name", errors_caught)
        self.assertIn("Not a valid value for category", errors_caught)
        self.assertIn("Not a valid value for b_range", errors_caught)

    @patch("sys.stdout", new_callable=StringIO)
    def test_budget_show_detailed_info(self, mock_stdout):
        self.obj.show_detailed_info()

        messages_caught = mock_stdout.getvalue().split("\n")

        self.assertIn(f'ID: {self.obj.id}', messages_caught)
        self.assertIn(f'Budget Name: {self.obj.name}', messages_caught)
        self.assertIn(f'Budget range: ({self.obj.b_range[0]} {self.obj.b_range[1]})', messages_caught)
        self.assertIn(f'Created at: {self.obj.created_at}', messages_caught)
