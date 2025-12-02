from ..models import Budget
from ..interfaces import ETControllerInterface
from ..utils.input_processors import string_input_processor, float_input_processor

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
            search_budget_by_name = budget_list.select_from_list(search_term=budget_name, search_by="name")
            if search_budget_by_name is None:
                print("Budget Name is valid")
                budget.name = budget_name
                is_valid_name = True
            else:
                print("Budget name is not valid: Try again")
            
        is_category_selected = False
        while is_category_selected == False:
            category_list.print_list()
            search_term = string_input_processor("Enter the category name or category id: ")

            search_category_by_name = category_list.select_from_list(search_term, search_by="name")
            search_category_by_id = category_list.select_from_list(search_term, search_by="id")
            if search_category_by_name is None and search_category_by_id is None:
                print("category not found: name and id are not valid")

            if search_category_by_name is not None and search_category_by_id is None:
                print(f"{search_category_by_name} found")
                budget.category = search_category_by_name
                is_category_selected = True

            if search_category_by_name is None and search_category_by_id is not None:
                print(f"{search_category_by_id} found")
                budget.category = search_category_by_id
                is_category_selected = True

        is_valid_range = False
        while is_valid_range == False:
            range_0 = float_input_processor("Enter the start of the budget range: ")
            range_1 = float_input_processor("Enter the end of the budget range: ")
            if range_0 < range_1 and range_1 > range_0:
                budget.b_range = (range_0, range_1)
                is_valid_range = True
            else:
                print("Budget range not valid: try again")
