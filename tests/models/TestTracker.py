import unittest
from unittest import TestCase
from src.expenses_tracker.models.Tracker import Tracker
from src.expenses_tracker.models.User import User
from src.expenses_tracker.models.Category import Category
from src.expenses_tracker.models.Budget import Budget
from src.expenses_tracker.models.Transaction import Transaction
from src.expenses_tracker.models.CategoryList import CategoryList
from src.expenses_tracker.models.BudgetList import BudgetList
from src.expenses_tracker.models.TransactionList import TransactionList

class TestTracker(TestCase):
    def setUp(self):
        test_user = User()
        test_category_list = CategoryList()
        test_budget_list = BudgetList()
        test_transaction_list = TransactionList()
        self.obj = Tracker(test_user, test_category_list, test_budget_list, test_transaction_list)

    def tearDown(self):
        self.obj = None

    def test_tracker_initilization(self):
        self.assertIsInstance(self.obj.user, User)
        self.assertIsInstance(self.obj.category_list, CategoryList)
        self.assertIsInstance(self.obj.budget_list, BudgetList)
        self.assertIsInstance(self.obj.transaction_list, TransactionList)

    def test_tracker_lists_uniqueness(self):
        new_category = Category()
        for i in range(2):
            self.obj.category_list.add_to_list(new_category)
        
        new_budget = Budget()
        for i in range(3):
            self.obj.budget_list.add_to_list(new_budget)

        new_transaction = Transaction()
        for i in range(4):
            self.obj.transaction_list.add_to_list(new_transaction)

        self.assertEqual(len(self.obj.category_list.collection), 2)
        self.assertEqual(len(self.obj.budget_list.collection), 3)
        self.assertEqual(len(self.obj.transaction_list.collection), 4)

if __name__ == "__main__":
    unittest.main()
