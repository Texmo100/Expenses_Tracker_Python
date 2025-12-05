from .helpers import *

def option_input_processor(message):
    while(True):
        try:
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input not valid: This is only white spaces or is an empty string')
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
                print('Input not valid: This is only white spaces or is an empty string')
                continue

            if is_valid_string(user_input):
                return user_input
            
            print("---- This string is not valid ----")

        except:
            print('Something went wrong: Enter characters only')
            print('\n')

def float_input_processor(message):
    while(True):
        try:
            user_input = input(message)

            if user_input.isspace() or user_input == "":
                print('Input not valid: This is only white spaces or is an empty string')
                continue

            user_input = float(user_input)
            if is_valid_currency(user_input):
                return user_input
            else:
                print('Input not valid: This might be zero. Enter just floating numbers only')
                continue

        except ValueError:
            print('Something went wrong: Enter numbers only')
            print('\n')
