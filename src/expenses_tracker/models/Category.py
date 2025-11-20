from ..interfaces import ETModelInterface
from random import randint
from ..utils import *

class Category(ETModelInterface):
    def __init__(self, name='', description='', limit=0):
        self._id = 'c00' + str(randint(1, 10000))
        self._name = name
        self._description = description
        self._limit = limit

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if is_valid_string(value):
            self._name = value
        else:
            print('Not a valid value for name')
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if is_valid_text(value):
            self._description = value
        else:
            print('Not a valid value for description')

    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self, value):
        if is_valid_currency(value):
            self._limit = value
        else:
            print('Not a valid value for limit')
    
    def show_detailed_info(self):
        print(f'ID: {self._id}')
        print(f'Name: {self._name}')
        print(f'Description: {self._description}')
        print(f'Budget Limit: {self._limit}')
