from models import User, Category, Budget, Transaction
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

    @property
    def transaction_history(self):
        return self.transaction_history
    
    @property
    def budget_list(self):
        return self.budget_list
    
    @property
    def category_list(self):
        return self.category_list

    def show_transaction_list(self):
        if len(self.transaction_history) > 0:
            for transaction in self.transaction_history:
                transaction.show_detailed_info()
                print('\n')
        else:
            print('No transactions to show')
    
    def select_transaction(self, transaction_id):
        if is_valid_string(transaction_id):
            target_transaction = [transaction for transaction in self.transaction_history if transaction_id == transaction.id]
            if len(target_transaction) > 0:
                return target_transaction[0]
            else:
                print('Transaction id not found')
                return None
        else:
            print('Transaction Id not valid')
            return None

    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.transaction_history.append(transaction)
        else:
            print('The transaction is not a valid type')
    
    def remove_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.transaction_history.remove(transaction)
        else:
            print('The transaction is not a valid type')

    def show_budget_list(self):
        if len(self.budget_list) > 0:
            for budget in self.budget_list:
                budget.show_detailed_info()
                print('\n')
        else:
            print('No budgets to show')

    def select_budget(self, search_term, search_by='id'):
        if is_valid_string(search_term):
            target_budget = []
            if search_by == 'id':
                target_budget = [budget for budget in self.budget_list if search_term == budget.id]
            
            if search_by == 'name':
                target_budget = [budget for budget in self.budget_list if search_term == budget.name]
            
            return target_budget[0] if len(target_budget) > 0 else None
        else:
            print('Search term is not valid')
            return None

    def add_budget(self, budget):
        if isinstance(budget, Budget):
            self.transaction_history.append(budget)
        else:
            print('The budget is not a valid type')
    
    def remove_budget(self, budget):
        if isinstance(budget, Budget):
            self.budget_list.remove(budget)
        else:
            print('The budget is not a valid type')

    def show_category_list(self):
        if len(self.category_list) > 0:
            for category in self.category_list:
                category.show_detailed_info()
                print('\n')
        else:
            print('No categories to show')

    def select_category(self, search_term, search_by='id'):
        if is_valid_string(search_term):
            target_category = []
            if search_by == 'id':
                target_category = [category for category in self.category_list if search_term == category.id]
            
            if search_by == 'name':
                target_category = [category for category in self.category_list if search_term == category.name]
            
            return target_category[0] if len(target_category) > 0 else None
        else:
            print('Search term is not valid')
            return None

    def add_category(self, category):
        if isinstance(category, Category):
            self.category_list.append(category)
        else:
            print('The category is not a valid type')
    
    def remove_category(self, category):
        if isinstance(category, Budget):
            self.category_list.remove(category)
        else:
            print('The category is not a valid type')
