from models import Category
from random import randint
from datetime import datetime
from utils import *

class Budget:
    def __init__(self, name='', category=None, b_range=(0, 0)):
        self._id = 'b00' + str(randint(1, 10000))
        self._name = name
        self._category = category
        self._b_range = b_range
        self._created_at = datetime.now()

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
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, Category):
            self._category = value
        else:
            print('Not a valid value for category')

    @property
    def b_range(self):
        return self._b_range
    
    @b_range.setter
    def b_range(self, value):
        if (is_valid_currency(value[0]) and value[0] > 0) and (is_valid_currency(value[1]) and value[1] > value[0]):
            self._b_range = value
        else:
            print('Not a valid value for b_range')

    def show_detailed_info(self):
        print(f'ID: {self._id}')
        print(f'Budget Name: {self._name}')
        print(f'Category name: {self._category}')
        print(f'Budget range: ({self._b_range[0]} {self._b_range[1]})')
        print(f'Created at: {self._created_at}')
