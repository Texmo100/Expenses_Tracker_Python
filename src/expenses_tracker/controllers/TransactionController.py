from models import Transaction
from interfaces import ETControllerInterface
from utils.input_processors import string_input_processor, float_input_processor

class TransactionController(ETControllerInterface):
    def create(self, category_list):
        new_transaction = Transaction()
        self._fill_info(new_transaction, category_list)
        print("New Transaction created successfully")
        return new_transaction

    def update(self, transaction, category_list):
        self._fill_info(transaction, category_list)
        print("Transaction updated successfully")

    def _fill_info(self, transaction, category_list):
        is_tranc_type_valid = False
        while is_tranc_type_valid == False:
            print("Options available:")
            print("- expense")
            print("+ income")
            tranc_type = string_input_processor("Enter the transaction type: ")
            if tranc_type.lower() == "expense" or tranc_type.lower() == "income":
                transaction.tranc_type = tranc_type
                is_tranc_type_valid = True
            else:
                print("Transaction type not valid. try again")

        transaction.amount = float_input_processor("Enter the transaction amount: ")

        is_category_selected = False
        while is_category_selected == False:
            category_list.print_list()
            search_term = string_input_processor("Enter the category name or category id: ")

            search_category_by_name = category_list.select_from_list(search_term, search_by="name")
            search_category_by_id = category_list.select_from_list(search_term, search_by="id")
            if search_category_by_name is None and search_category_by_id is None:
                print("category not found: name and id are not valid")

            if search_category_by_name is not None and search_category_by_id is None:
                print(f"{search_category_by_name} found")
                transaction.category = search_category_by_name
                is_category_selected = True

            if search_category_by_name is None and search_category_by_id is not None:
                print(f"{search_category_by_id} found")
                transaction.category = search_category_by_id
                is_category_selected = True

        is_payment_method_valid = False
        while is_payment_method_valid == False:
            print("Options available:")
            print("cash")
            print("credit card")
            payment_method = string_input_processor("Enter the payment method: ")
            if payment_method.lower() == "cash" or payment_method.lower() == "credit card":
                if payment_method == "credit card": payment_method = "credit_card"
                transaction.payment_method = payment_method
