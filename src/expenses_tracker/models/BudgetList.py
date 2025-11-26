from typing import override
from .ETListBase import ETListBase
from . import Budget

class BudgetList(ETListBase):
    @override
    def add_to_list(self, new_item):
        if isinstance(new_item, Budget):
            self._collection.append(new_item)
        else:
            print("Operation not allowed (Add): The new item is not a budget")

    @override
    def remove_from_list(self, item_to_remove):
        if isinstance(item_to_remove, Budget):
            self._collection.remove(item_to_remove)
        else:
            print("Operation not allowed (Delete): The new item is not a budget")
