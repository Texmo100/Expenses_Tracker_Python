from ..models import Budget
from ..interfaces import ETControllerInterface
from ..utils.input_processors import string_input_processor, float_input_processor
from ..utils.helpers import is_valid_name_in_collection, is_valid_range

class BudgetController(ETControllerInterface):
    def create(self, budget_list, category_list):
        new_budget = Budget()
        self._fill_info(new_budget, budget_list, category_list)
        print("New Budget created successfully")
        return new_budget

    def update(self, budget, budget_list, category_list):
        self._fill_info(budget, budget_list, category_list)
        print("Budget updated successfully")

    def _fill_info(self, budget, budget_list, category_list):
        is_valid_name = False
        while is_valid_name == False:
            budget_name = string_input_processor("Enter the budget name: ")
            is_valid_name = is_valid_name_in_collection(budget_name, budget_list)
        budget.name = budget_name
            
        is_category_selected = False
        while is_category_selected == False:
            category_list.print_list()
            category_name = string_input_processor("Enter the category name: ")

            search_category_by_name = category_list.select_from_list_by_name(category_name)
            if search_category_by_name is not None:
                budget.category = search_category_by_name
                is_category_selected = True
            
            if search_category_by_name is None:
                print("category not found")

        is_valid_budget_range = False
        while is_valid_budget_range == False:
            range_0 = float_input_processor("Enter the start of the budget range: ")
            range_1 = float_input_processor("Enter the end of the budget range: ")
            is_valid_budget_range = is_valid_range((range_0, range_1))
        budget.b_range = (range_0, range_1)
