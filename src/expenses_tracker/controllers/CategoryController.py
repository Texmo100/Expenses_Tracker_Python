from ..models.Category import Category
from ..interfaces.ETControllerInterface import ETControllerInterface
from ..utils.input_processors import string_input_processor, float_input_processor
from ..utils.helpers import *

class CategoryController(ETControllerInterface):
    def create(self, *args):
        new_category = Category()
        self._fill_info(new_category)
        print("New Category created sucessfully!")
        return new_category
    
    def update(self, model, *args):
        self._fill_info(model)
        print("Category updated sucessfully!")

    def _fill_info(self, model, *args):
        category_list = args[0]

        is_valid_name = False
        while is_valid_name == False:
            category_name = string_input_processor("Enter the category name: ")
            is_valid_name = is_valid_name_in_collection(category_name, category_list.collection)
        model.name = category_name

        model.description = string_input_processor("Enter the category description: ")
        model.limit = float_input_processor("Enter the category limit: ")
    