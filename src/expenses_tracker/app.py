from ui import *
from repositories import create_init_user, create_init_tracker
from utils.input_processors import option_input_processor

def app():
    user = create_init_user()
    tracker = create_init_tracker(user)

    is_exit = False
    while is_exit == False:
        main_menu_options = main_menu()
        menu_printer(main_menu_options)
        option_selected = option_input_processor('Enter the option: ')

        if option_selected == 0:
            is_exit = True
        
        if option_selected > 0 and option_selected < len(main_menu_options):
            is_back = False
            while is_back == False:
                option_selected_name = main_menu_options[option_selected]
                sub_menu_options = sub_menu(option_selected_name)
                menu_printer(sub_menu_options, type='sub_menu', option_selected_name=option_selected_name)
                sub_option_selected = option_input_processor('Enter the option: ')

                if sub_option_selected == 0:
                    is_back = True

                if sub_option_selected > 0 and sub_option_selected < len(sub_menu_options):
                    print(f'You selected {sub_menu_options[sub_option_selected]}')

                if sub_option_selected > len(sub_menu_options) - 1:
                    print('\n')
                    print('-----------------------')
                    print(' Option not recognized ')
                    print('-----------------------')

        if option_selected > len(main_menu_options) - 1:
            print('\n')
            print('-----------------------')
            print(' Option not recognized ')
            print('-----------------------')
