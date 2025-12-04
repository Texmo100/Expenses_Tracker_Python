from ..models.Category import Category
from ..interfaces.ETControllerInterface import ETControllerInterface
from ..utils.input_processors import string_input_processor, float_input_processor

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
        model.name = string_input_processor("Enter the category name: ")
        model.description = string_input_processor("Enter the category description: ")
        model.limit = float_input_processor("Enter the category limit: ")
    