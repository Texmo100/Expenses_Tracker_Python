from random import randint

class Tracker:
    def __init__(self, user, category_list, budget_list, transaction_list):
        self._id = 'track00' + str(randint(1, 10000))
        self._user = user
        self._category_list = category_list
        self._budget_list = budget_list
        self._transaction_list = transaction_list

    @property
    def id(self):
        return self._id
    
    @property
    def user(self):
        return self._user
    
    @property
    def category_list(self):
        return self._category_list
    
    @property
    def budget_list(self):
        return self._budget_list
    
    @property
    def transaction_list(self):
        return self._transaction_list
