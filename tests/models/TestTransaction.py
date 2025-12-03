from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.interfaces.ETModelInterface import ETModelInterface
from src.expenses_tracker.models.Transaction import Transaction
from src.expenses_tracker.models.Category import Category
from datetime import date

class TestTransaction(TestCase):
    def setUp(self):
        category_test = Category()
        self.obj = Transaction("sword","expense", 100.0, category_test, "cash")

    def tearDown(self):
        self.obj = None

    def test_transaction_initialization(self):
        self.assertIsInstance(self.obj, Transaction)
        self.assertEqual(self.obj.name, "sword")
        self.assertEqual(self.obj.tranc_type, "expense")
        self.assertEqual(self.obj.amount, 100.0)
        self.assertIsInstance(self.obj.category, Category)
        self.assertEqual(self.obj.date, date.today())
        self.assertEqual(self.obj.payment_method, "cash")

    def test_transaction_setters_with_valid_values(self):
        new_category = Category()

        self.obj.name = "big sword"
        self.obj.tranc_type = "income"
        self.obj.amount = 5000.00
        self.obj.category = new_category
        self.obj.payment_method = "credit card"

        self.assertEqual(self.obj.name, "big sword")
        self.assertEqual(self.obj.tranc_type, "income")
        self.assertEqual(self.obj.amount, 5000.00)
        self.assertIsInstance(self.obj.category, Category)
        self.assertEqual(self.obj.date, date.today())
        self.assertEqual(self.obj.payment_method, "credit card")

    @patch("sys.stdout", new_callable=StringIO)
    def test_transaction_setters_with_invalid_values(self, mock_stdout):
        new_false_category = Transaction()

        self.obj.name = "7983789132789312"
        self.obj.tranc_type = "large income"
        self.obj.amount = 0
        self.obj.category = new_false_category
        self.obj.payment_method = "0813989083"

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Not a valid value for tranc_type", error_messages)
        self.assertIn("Not a valid value for amount", error_messages)
        self.assertIn("Not a valid value for category", error_messages)
        self.assertIn("Not a valid value for payment_method", error_messages)

    @patch("sys.stdout", new_callable=StringIO)
    def test_transaction_show_detailed_info(self, mock_stdout):
        self.obj.show_detailed_info()

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn(f'ID: {self.obj.id}', messages)
        self.assertIn(f'Transaction Name: {self.obj.name}', messages)
        self.assertIn(f'Transaction type: {self.obj.tranc_type}', messages)
        self.assertIn(f'Amount: {self.obj.amount}', messages)
        self.assertIn(f'Category: {self.obj.category}', messages)
        self.assertIn(f'Date: {self.obj.date}', messages)
        self.assertIn(f'Payment Method: {self.obj.payment_method}', messages)
