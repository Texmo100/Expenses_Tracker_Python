import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.ui.ui import main_menu, sub_menu, menu_printer

class TestUi(TestCase):
    def test_main_menu(self):
        test_main_menu_options = {
            0: 'exit',
            1: 'categories',
            2: 'budgets',
            3: 'transactions'
        }

        main_menu_options = main_menu()

        self.assertIsInstance(main_menu_options, dict)
        self.assertDictEqual(main_menu_options, test_main_menu_options)

    def test_sub_menu(self):
        test_option_selected = "categories"
        test_sub_menu_options = {
            0: 'Main menu',
            1: f'Show categories',
            2: f'Create category',
            3: f'Modify category',
            4: f'Delete category'
        }

        sub_menu_options = sub_menu(test_option_selected)

        self.assertIsInstance(sub_menu_options, dict)
        self.assertDictEqual(sub_menu_options, test_sub_menu_options)

    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_printer_with_main_menu(self, mock_stdout):
        main_menu_options = main_menu()
        menu_printer(main_menu_options)

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Welcome to Expenses Tracker ------ Y", messages)
        self.assertIn("------------ Main Menu -------------", messages)
        self.assertIn("0: Exit", messages)
        self.assertIn("1: Categories", messages)
        self.assertIn("2: Budgets", messages)
        self.assertIn("3: Transactions", messages)
        self.assertIn("------------------------------------", messages)

    @patch("sys.stdout", new_callable=StringIO)
    def test_menu_printer_with_sub_menu(self, mock_stdout):
        test_selected_option = "categories"
        sub_menu_options = sub_menu(test_selected_option)
        menu_printer(sub_menu_options, "sub_menu", test_selected_option)

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Categories Menu", messages)
        self.assertIn("0: Main menu", messages)
        self.assertIn("1: Show categories", messages)
        self.assertIn("2: Create category", messages)
        self.assertIn("3: Modify category", messages)
        self.assertIn("4: Delete category", messages)
        self.assertIn("-------------------------------", messages)

if __name__ == "__main__":
    unittest.main()
