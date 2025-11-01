from utils.helpers import *

def option_input_processor(message):
    while(True):
        try:
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input not valid')
                continue

            user_input = int(user_input)
            if is_valid_integer(user_input):
                return user_input
            else:
                print('Input not valid')
                continue
                
        except ValueError:
            print('Something went wrong: Enter numbers only')
            print('\n')

def string_input_processor(message):
    while(True):
        try:
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input is not valid')
                continue

            if is_valid_string(user_input):
                return user_input
            elif is_valid_text(user_input):
                return user_input
            else:
                print('Input not valid')
                continue

        except TypeError:
            print('Something went wrong: Enter characters only')
            print('\n')

def float_input_processor(message):
    while(True):
        try:
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input is not valid')
                continue

            user_input = float(user_input)
            if is_valid_currency(user_input):
                return user_input
            else:
                print('Input is not valid')
                continue

        except TypeError:
            print('Something went wrong: Enter numbers only')
            print('\n')
