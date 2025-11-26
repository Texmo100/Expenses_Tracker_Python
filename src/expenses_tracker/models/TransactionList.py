from typing import override
from .ETListBase import ETListBase
from . import Transaction

class TransactionList(ETListBase):
    @override
    def add_to_list(self, new_item):
        if isinstance(new_item, Transaction):
            self._collection.append(new_item)
        else:
            print("Operation not allowed (Add): The new item is not a transaction")

    @override
    def remove_from_list(self, item_to_remove):
        if isinstance(item_to_remove, Transaction):
            self._collection.remove(item_to_remove)
        else:
            print("Operation not allowed (Delete): The new item is not a transaction")