def main_menu():
    main_menu_options = {
        0: 'exit',
        1: 'categories',
        2: 'budgets',
        3: 'transactions'
    }

    return main_menu_options

def sub_menu(selected_option_name):
    sub_menu_options = {
        0: 'Main menu',
        1: f'Show',
        2: f'Create',
        3: f'Modify',
        4: f'Delete'
    }

    # Formating and replacing placeholders
    for key, value in sub_menu_options.items():
        if key > 0:
            if selected_option_name == "categories":
                new_value = f"{value} {(selected_option_name[:-3] + "y" if key > 1 else selected_option_name)}"
                sub_menu_options[key] = new_value
            else:
                new_value = f"{value} {(selected_option_name[:-1] if key > 1 else selected_option_name)}"
                sub_menu_options[key] = new_value

    return sub_menu_options

def menu_printer(options, type='main_menu', option_selected_name=None):
    if type == 'main_menu' and option_selected_name == None:
        print('\n')
        print('Welcome to Expenses Tracker ------ Y')
        print('------------ Main Menu -------------')
        for key, value in options.items():
            print(f'{key}: {value.capitalize()}')
        print('------------------------------------')
    
    if type == 'sub_menu' and option_selected_name != None:
        print('\n')
        print(f'{option_selected_name.capitalize()} Menu')
        print('-------------------------------')
        for key, value in options.items():
            print(f'{key}: {value}')
        print('-------------------------------')
