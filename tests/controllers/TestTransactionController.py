import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.expenses_tracker.controllers.TransactionController import TransactionController
from src.expenses_tracker.models.Transaction import Transaction
from src.expenses_tracker.models.TransactionList import TransactionList
from src.expenses_tracker.models.CategoryList import CategoryList

class TestTransactionController(TestCase):
    def setUp(self):
        self.obj = TransactionController()

    def tearDown(self):
        self.obj = None

    @patch("builtins.print")
    @patch.object(TransactionController,"_fill_info")
    def test_create(self, mock_fill_info, mock_print):
        test_transaction_list = MagicMock(spec=TransactionList)
        test_category_list = MagicMock(spec=CategoryList)
        
        test_transaction = self.obj.create(test_transaction_list, test_category_list)

        self.assertIsInstance(test_transaction, Transaction)
        mock_fill_info.assert_called_once_with(test_transaction, test_transaction_list, test_category_list)
        mock_print.assert_called_once_with("New Transaction created successfully")
    
    @patch("builtins.print")
    @patch.object(TransactionController,"_fill_info")
    def test_update(self, mock_fill_info, mock_print):
        test_transaction = MagicMock(spec=Transaction)
        test_transaction_list = MagicMock(spec=TransactionList)
        test_category_list = MagicMock(spec=CategoryList)
        
        self.obj.update(test_transaction, test_transaction_list, test_category_list)

        mock_fill_info.assert_called_once_with(test_transaction, test_transaction_list, test_category_list)
        mock_print.assert_called_once_with("Transaction updated successfully")

    @patch("src.expenses_tracker.controllers.TransactionController.is_valid_payment_method")
    @patch("src.expenses_tracker.controllers.TransactionController.float_input_processor")
    @patch("src.expenses_tracker.controllers.TransactionController.is_valid_tranc_type")
    @patch("src.expenses_tracker.controllers.TransactionController.is_valid_name_in_collection")
    @patch("src.expenses_tracker.controllers.TransactionController.string_input_processor")
    def test_fill_info(self, mock_string_processor, mokc_is_valid_name, mock_valid_tranc_type, mock_float_processor, mock_valid_payment_method):
        mock_string_processor.side_effect = ["videogame","income", "fun", "cash"]
        mokc_is_valid_name.return_value = True
        mock_valid_tranc_type.return_value = True
        mock_float_processor.return_value = 100.0
        mock_valid_payment_method.return_value = True

        test_transaction = MagicMock(spec=Transaction)
        test_transaction_list = MagicMock(spec=TransactionList)
        test_category_list = MagicMock(spec=CategoryList)
        self.obj._fill_info(test_transaction, test_transaction_list, test_category_list)

        self.assertEqual(test_transaction.name, "videogame")
        self.assertEqual(test_transaction.tranc_type, "income")
        self.assertEqual(test_transaction.payment_method, "cash")

        mock_string_processor.assert_any_call("Enter the transaction name: ")
        mock_string_processor.assert_any_call("Enter the transaction type: ")
        mock_string_processor.assert_any_call("Enter the category name: ")
        mock_valid_tranc_type.assert_called_once()
        mock_float_processor.assert_any_call("Enter the transaction amount: ")
        mock_valid_payment_method.assert_called_once()
    
if __name__ == "__main__":
    unittest.main()
