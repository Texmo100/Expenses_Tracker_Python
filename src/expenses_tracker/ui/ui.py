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
        1: f'Show <place-holder>',
        2: f'Create new <place-holder>',
        3: f'Modify a <place-holder>',
        4: f'Delete a <place-holder>'
    }

    # Formating and replacing placeholders
    for key, value in sub_menu_options.items():
        if key == 1:
            new_value = value.replace('<place-holder>', selected_option_name)
            sub_menu_options[key] = new_value

        if key > 1 and selected_option_name == 'categories':
            new_value = value.replace('<place-holder>', 'category')
            sub_menu_options[key] = new_value

        if key > 1 and selected_option_name != 'categories':
            new_value = value.replace('<place-holder>', selected_option_name[:-1])
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
