import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.expenses_tracker.controllers.BudgetController import BudgetController
from src.expenses_tracker.models.Budget import Budget
from src.expenses_tracker.models.BudgetList import BudgetList
from src.expenses_tracker.models.CategoryList import CategoryList

class TestBudgetController(TestCase):
    def setUp(self):
        self.obj = BudgetController()

    def tearDown(self):
        self.obj = None

    @patch("builtins.print")
    @patch.object(BudgetController, "_fill_info")
    def test_create(self, mock_fill_info, mock_print):
        test_budget_list = MagicMock(spec=BudgetList)
        test_category_list = MagicMock(spec=CategoryList)

        test_budget = self.obj.create(test_budget_list, test_category_list)

        self.assertIsInstance(test_budget, Budget)
        mock_fill_info.assert_called_once_with(test_budget, test_budget_list, test_category_list)
        mock_print.assert_called_once_with("New Budget created successfully")
    
    @patch("builtins.print")
    @patch.object(BudgetController, "_fill_info")
    def test_update(self, mock_fill_info, mock_print):
        test_budget_list = MagicMock(spec=BudgetList)
        test_category_list = MagicMock(spec=CategoryList)
        test_budget = MagicMock(spec=Budget)

        self.obj.update(test_budget, test_budget_list, test_category_list)

        mock_fill_info.assert_called_once_with(test_budget, test_budget_list, test_category_list)
        mock_print.assert_called_once_with("Budget updated successfully")

    @patch("src.expenses_tracker.controllers.BudgetController.is_valid_range")
    @patch("src.expenses_tracker.controllers.BudgetController.float_input_processor")
    @patch("src.expenses_tracker.controllers.BudgetController.is_valid_name_in_collection")
    @patch("src.expenses_tracker.controllers.BudgetController.string_input_processor")
    def test_fill_info(self, mock_string_processor, mock_validname, mock_float_processor, mock_validrange):
        mock_string_processor.side_effect = ["games", "fun"]
        mock_validname.return_value = True
        mock_float_processor.side_effect = [100.0, 1000.0]
        mock_validrange.return_value = True

        test_budget = MagicMock(spec=Budget)
        test_budget_list = MagicMock(spec=BudgetList)
        test_category_list = MagicMock(spec=CategoryList)
        self.obj._fill_info(test_budget, test_budget_list, test_category_list)

        self.assertEqual(test_budget.name, "games")
        self.assertEqual(test_budget.b_range[0], 100.0)
        self.assertEqual(test_budget.b_range[1], 1000.0)

        mock_string_processor.assert_any_call("Enter the budget name: ")
        mock_string_processor.assert_any_call("Enter the category name: ")
        mock_validname.assert_called_once()
        mock_float_processor.assert_any_call("Enter the start of the budget range: ")
        mock_float_processor.assert_any_call("Enter the end of the budget range: ")
        mock_validrange.assert_called_once()

if __name__ == "__main__":
    unittest.main()
