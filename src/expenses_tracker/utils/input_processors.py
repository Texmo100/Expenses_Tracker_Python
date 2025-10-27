from utils.helpers import *

def option_input_processor(message):
    try:
        while(True):
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input is invalid')
                continue

            user_input = int(user_input)
            if is_valid_integer(user_input):
                return user_input
            else:
                print('Input not valid')
            
    except TypeError:
        print('Something went wrong: Enter numbers only')

def string_input_processor(message):
    try: 
        while(True):
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input is invalid')
                continue

            if is_valid_string(user_input):
                return user_input
            elif is_valid_text(user_input):
                return user_input
            else:
                print('Input not valid')

    except TypeError:
        print('Something went wrong: Enter characters only')

def float_input_processor(message):
    try: 
        while(True):
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input is invalid')
                continue

            user_input = float(user_input)
            if is_valid_currency(user_input):
                return user_input
            else:
                print('Input not valid')

    except TypeError:
        print('Something went wrong: Enter numbers only')
