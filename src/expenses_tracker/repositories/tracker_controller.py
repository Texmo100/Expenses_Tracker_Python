from models import *
from utils.input_processors import *

def create_init_user():
    user = User('isaac', 'iniguez', '6621194658', 'luna olivarria 245')
    return user

def create_init_tracker(user):
    tracker = Tracker(user)
    return tracker

def show_list(tracker, type_list):
    if type_list == 'categories':
        tracker.show_category_list()
    
    if type_list == 'budgets':
        tracker.show_budget_list()

    if type_list == 'transactions':
        tracker.show_transaction_list()

    if type_list == '' or type_list.isspace():
        print('List not recognized')

def add_item_to_list(tracker, type_list):
    if type_list == 'categories':
        is_valid_name = False
        while is_valid_name == False:
            name = string_input_processor('Enter the category name: ')
            if tracker.select_category(name, search_by='name'):
                print('Name is valid')
                is_valid_name = True
            else:
                print('Name is not valid')
        desc = string_input_processor('Enter the description of the category: ')
        limit = float_input_processor('Enter the limit of the category: ')
        new_category = Category(name, desc, limit)
        tracker.add_category(new_category)
        print(f'{name} added to the categories list')

    
    if type_list == 'budgets':
        tracker.show_budget_list()

    if type_list == 'transactions':
        tracker.show_transaction_list()

    if type_list == '' or type_list.isspace():
        print('List not recognized')
    