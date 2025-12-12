from src.expenses_tracker.models.User import User
from src.expenses_tracker.models.CategoryList import CategoryList
from src.expenses_tracker.models.BudgetList import BudgetList
from src.expenses_tracker.models.TransactionList import TransactionList
from src.expenses_tracker.models.Tracker import Tracker

from src.expenses_tracker.controllers.CategoryController import CategoryController
from src.expenses_tracker.controllers.BudgetController import BudgetController
from src.expenses_tracker.controllers.TransactionController import TransactionController

from src.expenses_tracker.ui.ui import *
from src.expenses_tracker.utils.input_processors import *

def main():
    tracker = tracker_initialization()

    while True:
        option_selected = main_menu_executor(main_menu())
        if option_selected == "exit": break

        if len(tracker.category_list.collection) == 0 and (option_selected != "categories" and option_selected != "exit"):
            print(" ---- Option not available: You must create categories to access to this options ---- ")
            print("\n")
        else:
            model_list = None
            model_list_dependency = tracker.category_list
            model_controller = None

            if option_selected == "categories": 
                model_list = tracker.category_list
                model_controller = CategoryController()
            if option_selected == "budgets": 
                model_list = tracker.budget_list
                model_controller = BudgetController()
            if option_selected == "transactions": 
                model_list = tracker.transaction_list
                model_controller = TransactionController()

            sub_menu_executor(option_selected, sub_menu(option_selected), model_list, model_list_dependency, model_controller)

def tracker_initialization():
    tracker = Tracker(
        User("isaac", "iniguez", "6645237867", "lagos de rosa"),
        CategoryList(),
        BudgetList(),
        TransactionList()
    )

    return tracker

def main_menu_executor(main_menu_options):
    is_option_selected = False
    while is_option_selected == False:
        menu_printer(main_menu_options)
        user_input = option_input_processor("Select the option from the menu: ", num_options=len(main_menu_options))
        
        option_selected = main_menu_options[user_input]
        is_option_selected = True

        return option_selected
    
def sub_menu_executor(option_selected, sub_menu_options, model_list, model_list_dependency, model_controller):
    is_backto_mainmenu = False
    while is_backto_mainmenu == False:
        menu_printer(sub_menu_options, "sub_menu", option_selected)
        action_selected = option_input_processor("Enter the action from the menu: ", num_options=len(sub_menu_options))
        
        if action_selected == 0: is_backto_mainmenu = True
        if action_selected == 1: model_list.print_detailed_list()
        if action_selected == 2: create_executor(model_list, model_list_dependency, model_controller)
        if action_selected == 3: update_executor(model_list, model_list_dependency, model_controller)
        if action_selected == 4: delete_executor(model_list)
    

def create_executor(model_list, model_list_dependency, model_controller):
    new_model_item = model_controller.create(model_list, model_list_dependency)
    model_list.add_to_list(new_model_item)

def update_executor(model_list, model_list_dependency, model_controller):
    if len(model_list.collection) == 0:
        print("Update is not available: You must create an item first")
    else:
        model_item = find_item_in_model_list(model_list)
        model_controller.update(model_item, model_list, model_list_dependency)

def delete_executor(model_list):
    if len(model_list.collection) == 0:
        print("Delete is not available: You must create an item first")
    else:
        model_item = find_item_in_model_list(model_list)
        model_list.remove_from_list(model_item)
        model_item = None

def find_item_in_model_list(model_list):
    existing_model_item = None

    item_found = False
    while item_found == False:
        model_list.print_short_list()
        model_item_name = string_input_processor("Enter the name of the item: ")
        existing_model_item = model_list.select_from_list_by_name(model_item_name)
        if existing_model_item != None: item_found = True
        if existing_model_item == None: print("Item not found: item name misspelled or not in collection")
    
    return existing_model_item

if __name__ == '__main__':
    main()
