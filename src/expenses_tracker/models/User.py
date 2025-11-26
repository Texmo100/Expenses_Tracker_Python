from random import randint
from ..utils import *

class User:
    def __init__(self, firstname='', lastname='', phone_number='', address=''):
        self._id = 'u00' + str(randint(1, 10000))
        self._firstname = firstname
        self._lastname = lastname
        self._phone_number = phone_number
        self._address = address
        
    @property
    def id(self):
        return self._id
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, value):
        if is_valid_string(value):
            self._firstname = value
        else:
            print('Not a valid value for firstname')


    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value):
        if is_valid_string(value):
            self._lastname = value
        else:
            print('Not a valid value for lastname')

    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        if is_valid_phone_number(value):
            self._phone_number = value
        else:
            print('Not a valid value for phone_number')

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        if is_valid_text(value):
            self._address = value
        else:
            print('Not a valid value for address')
