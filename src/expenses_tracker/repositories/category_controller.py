from models import *
from utils.input_processors import *

def create_new_category():
    try:
        name = string_input_processor('Enter the category name: ')
        desc = string_input_processor('Enter the description of the category: ')
        limit = float_input_processor('Enter the limit of the category: ')

        new_category = Category()
        new_category.name = name
        new_category.description = desc
        new_category.limit = limit

        new_category.show_category_info()

        return new_category

    except:
        print('Something went wrong during this operation: Try again')
