from ..interfaces import ETModelInterface
from .Category import Category
from random import randint
from datetime import date
from ..utils import *

class Transaction(ETModelInterface):
    def __init__(self, tranc_type='', amount=0, category=None, payment_method=''):
        self._id = 't00' + str(randint(1, 10000))
        self._tranc_type = tranc_type
        self._amount = amount
        self._category = category
        self._date = date.today()
        self._payment_method = payment_method

    @property
    def id(self):
        return self._id
    
    @property
    def tranc_type(self):
        return self._tranc_type
    
    @tranc_type.setter
    def tranc_type(self, value):
        if is_valid_string(value) and (value == "income" or value == "expense"):
            self._tranc_type = value
        else:
            print('Not a valid value for tranc_type')

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if is_valid_currency(value):
            if self._tranc_type == 'expense':
                self._amount = value * -1
            elif self._tranc_type == 'income':
                self._amount = value
        else:
            print("Not a valid value for amount")

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
    def date(self):
        return self._date

    @property
    def payment_method(self):
        return self._payment_method
    
    @payment_method.setter
    def payment_method(self, value):
        if is_valid_string(value) and (value == "cash" or value == "credit card"):
            self._payment_method = value
        else:
            print('Not a valid value for payment_method')

    def show_detailed_info(self):
        print(f'ID: {self._id}')
        print(f'Transaction type: {self._tranc_type}')
        print(f'Amount: {self._amount}')
        print(f'Category: {self._category}')
        print(f'Date: {self._date}')
        print(f'Payment Method: {self._payment_method}')
