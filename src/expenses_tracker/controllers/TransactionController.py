from ..models.TransactionList import TransactionList
from ..models.Transaction import Transaction
from ..interfaces.ETControllerInterface import ETControllerInterface
from ..utils.helpers import *
from ..utils.input_processors import string_input_processor, float_input_processor

class TransactionController(ETControllerInterface):
    def create(self, *args):
        transaction_list, category_list = args

        new_transaction = Transaction()
        self._fill_info(new_transaction, transaction_list, category_list)
        print("New Transaction created successfully")
        return new_transaction

    def update(self, model, *args):
        transaction_list, category_list = args

        self._fill_info(model, transaction_list, category_list)
        print("Transaction updated successfully")

    def _fill_info(self, model, *args):
        transaction_list, category_list = args

        is_valid_tranc_name = False
        while is_valid_tranc_name == False:
            transaction_name = string_input_processor("Enter the transaction name: ")
            is_valid_tranc_name = is_valid_name_in_collection(transaction_name, transaction_list.collection)
        model.name = transaction_name

        is_valid_transaction_type = False
        while is_valid_transaction_type == False:
            print("Options available:")
            print("- expense")
            print("+ income")
            tranc_type = string_input_processor("Enter the transaction type: ")
            is_valid_transaction_type = is_valid_tranc_type(tranc_type)
        model.tranc_type = tranc_type

        model.amount = float_input_processor("Enter the transaction amount: ")

        is_category_selected = False
        while is_category_selected == False:
            category_list.print_list()
            category_name = string_input_processor("Enter the category name: ")

            search_category_by_name = category_list.select_from_list_by_name(category_name)
            if search_category_by_name is not None:
                model.category = search_category_by_name
                is_category_selected = True

            if search_category_by_name is None:
                print("category not found: name and id are not valid")

        is_payment_method_valid = False
        while is_payment_method_valid == False:
            print("Options available:")
            print("cash")
            print("credit card")
            payment_method = string_input_processor("Enter the payment method: ")
            is_payment_method_valid = is_valid_payment_method(payment_method)
        model.payment_method = payment_method
        