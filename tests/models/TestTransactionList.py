import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.models.TransactionList import TransactionList
from src.expenses_tracker.models.Category import Category
from src.expenses_tracker.models.Transaction import Transaction

class TestTransactionList(TestCase):
    def setUp(self):
        self.obj = TransactionList()

    def tearDown(self):
        self.obj = None

    def test_transactionlist_initialization(self):
        self.assertIsInstance(self.obj, TransactionList)
        self.assertIsInstance(self.obj.collection, list)
    
    def test_transactionlist_add_with_valid_values(self):
        new_transaction = Transaction()
        self.obj.add_to_list(new_transaction)

        self.assertIn(new_transaction, self.obj.collection)

    @patch("sys.stdout", new_callable=StringIO)
    def test_transactionlist_add_with_invalid_values(self, mock_stdout):
        fake_transaction = "fake transaction"

        self.obj.add_to_list(fake_transaction)

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Operation not allowed (Add): The new item is not a transaction", error_messages)

    def test_transactionlist_select_from_list_by_name(self):
        category = Category()
        new_transaction = Transaction("sword", "expense", 100.0, category, "cash")
        self.obj.add_to_list(new_transaction)

        selected_transaction_by_name = self.obj.select_from_list_by_name(new_transaction.name)

        self.assertEqual(selected_transaction_by_name, new_transaction)

    @patch("sys.stdout", new_callable=StringIO)
    def test_transactionlist_print_short_list(self, mock_stdout):
        category = Category()
        new_transaction = Transaction("game", "expense", 100.0, category, "cash")
        self.obj.add_to_list(new_transaction)

        self.obj.print_short_list()

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn(f'{self.obj.collection[0].id}: {self.obj.collection[0].name}', messages)
    
    @patch("sys.stdout", new_callable=StringIO)
    def test_transactionlist_print_detailed_list(self, mock_stdout):
        category = Category("games")
        new_transaction = Transaction("game", "expense", 100.0, category, "cash")
        self.obj.add_to_list(new_transaction)

        self.obj.print_detailed_list()

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn(f'ID: {self.obj.collection[0].id}', messages)
        self.assertIn(f'Transaction Name: {self.obj.collection[0]._name}', messages)
        self.assertIn(f'Transaction type: {self.obj.collection[0].tranc_type}', messages)
        self.assertIn(f'Amount: {self.obj.collection[0].amount}', messages)
        self.assertIn(f'Category: {self.obj.collection[0].category.name}', messages)
        self.assertIn(f'Date: {self.obj.collection[0].date}', messages)
        self.assertIn(f'Payment Method: {self.obj.collection[0].payment_method}', messages)

    def test_transactionlist_remove(self):
        category = Category()
        transaction = Transaction("expense", 100.0, category, "cash")
        self.obj.add_to_list(transaction)

        self.obj.remove_from_list(transaction)

        self.assertNotIn(transaction, self.obj.collection)

    @patch("sys.stdout", new_callable=StringIO)
    def test_transactionlist_remove_no_valid_items(self, mock_stdout):
        fake_transaction = "fake transaction"
        self.obj.remove_from_list(fake_transaction)

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Operation not allowed (Delete): The new item is not a transaction", error_messages)

if __name__ == "__main__":
    unittest.main()
