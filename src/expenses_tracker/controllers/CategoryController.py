from models import Category
from interfaces import ETControllerInterface
from utils.input_processors import string_input_processor, float_input_processor

class CategoryController(ETControllerInterface):
    def create(self):
        new_category = Category()
        self._fill_info(new_category)
        print("New Category created sucessfully!")
        return new_category
    
    def update(self, category):
        self._fill_info(category)
        print("Category updated sucessfully!")

    def _fill_info(self, category):
        category.name = string_input_processor("Enter the category name: ")
        category.description = string_input_processor("Enter the category description: ")
        category.limit = float_input_processor("Enter the category limit: ")
    