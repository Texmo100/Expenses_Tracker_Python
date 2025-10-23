import User
import Transaction
import Budget
import Category
from random import randint
from utils import *

class Tracker:
    def __init__(self, user=None):
        self._id = 'track00' + str(randint(1, 10000))
        self._user = user
        self.transaction_history = []
        self.budget_list = []
        self.category_list = []

    @property
    def id(self):
        return self._id
    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, new_user):
        if isinstance(new_user, User):
            self._user = new_user
        else:
            print('Not a valid value for user')

    def show_transaction_list(self):
        if len(self.transaction_history) > 0:
            for transaction in self.transaction_history:
                transaction.show_transaction_info()
                print('\n')
        else:
            print('No transactions to show')

    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.transaction_history.append(transaction)
        else:
            print('The transaction is not a valid type')
    
    def remove_transaction(self, transaction_id):
        if is_valid_string(transaction_id):
            target_transaction = [transaction for transaction in self.transaction_history if transaction_id == transaction.id]
            if len(target_transaction) > 0:
                self.transaction_history.remove(target_transaction[0])
            else:
                print('Transaction id not found')

    def show_budget_list(self):
        if len(self.budget_list) > 0:
            for budget in self.budget_list:
                budget.show_budget_info()
                print('\n')
        else:
            print('No budgets to show')

    def add_budget(self, budget):
        if isinstance(budget, Budget):
            self.transaction_history.append(budget)
        else:
            print('The budget is not a valid type')
    
    def remove_budget(self, budget_id):
        if is_valid_string(budget_id):
            target_budget = [budget for budget in self.budget_list if budget_id == budget.id]
            if len(target_budget) > 0:
                self.budget_list.remove(target_budget[0])
            else:
                print('Budget id not found')

    def show_category_list(self):
        if len(self.category_list) > 0:
            for category in self.category_list:
                category.show_category_info()
                print('\n')
        else:
            print('No categories to show')

    def add_category(self, category):
        if isinstance(category, Category):
            self.category_list.append(category)
        else:
            print('The category is not a valid type')
    
    def remove_category(self, category_id):
        if is_valid_string(category_id):
            target_category = [category for category in self.category_list if category_id == category.id]
            if len(target_category) > 0:
                self.budget_list.remove(target_category[0])
            else:
                print('Category id not found')
