import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.models.BudgetList import BudgetList
from src.expenses_tracker.models.Category import Category
from src.expenses_tracker.models.Budget import Budget

class TestBudgetList(TestCase):
    def setUp(self):
        self.obj = BudgetList()

    def tearDown(self):
        self.obj = None

    def test_budgetlist_initialization(self):
        self.assertIsInstance(self.obj, BudgetList)
        self.assertIsInstance(self.obj.collection, list)
    
    def test_budgetlist_add_with_valid_values(self):
        new_category = Budget()
        self.obj.add_to_list(new_category)

        self.assertIn(new_category, self.obj.collection)

    @patch("sys.stdout", new_callable=StringIO)
    def test_budgetlist_add_with_invalid_values(self, mock_stdout):
        fake_budget = Category()

        self.obj.add_to_list(fake_budget)

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Operation not allowed (Add): The new item is not a budget", error_messages)

    def test_budgetlist_select_from_list_by_name(self):
        category = Category()
        new_budget = Budget("home", category, (500.0, 1000.0))
        self.obj.add_to_list(new_budget)

        selected_budget_by_name = self.obj.select_from_list_by_name("home")

        self.assertEqual(selected_budget_by_name, new_budget)

    @patch("sys.stdout", new_callable=StringIO)
    def test_budgetlist_print_list(self, mock_stdout):
        category = Category()
        new_budget = Budget("home", category, (500.0, 1000.0))
        self.obj.add_to_list(new_budget)

        self.obj.print_list()

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn(f'ID: {self.obj.collection[0].id}', messages)
        self.assertIn(f'Budget Name: {self.obj.collection[0].name}', messages)
        self.assertIn(f'Budget range: ({self.obj.collection[0].b_range[0]} {self.obj.collection[0].b_range[1]})', messages)
        self.assertIn(f'Created at: {self.obj.collection[0].created_at}', messages)

    def test_budgetlist_remove(self):
        category = Category()
        budget = Budget("home", category, (500.0, 1000.0))
        self.obj.add_to_list(budget)

        self.obj.remove_from_list(budget)

        self.assertNotIn(budget, self.obj.collection)

    @patch("sys.stdout", new_callable=StringIO)
    def test_budgetlist_remove_no_valid_items(self, mock_stdout):
        fake_budget = "fake budget"
        self.obj.remove_from_list(fake_budget)

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Operation not allowed (Delete): The new item is not a budget", error_messages)

if __name__ == "__main__":
    unittest.main()
