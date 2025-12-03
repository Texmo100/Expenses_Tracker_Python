import re

def is_valid_string(string):
    if isinstance(string, str):
        pattern = r"^[a-zA-Z\s]+$"

        full_match = re.fullmatch(pattern, string)
        is_valid = True if full_match is not None else False

        return is_valid
    else:
        return False

def is_valid_text(text):
    if isinstance(text, str) and text.count(" ") > 0:
        return True
    else:
        return False

def is_valid_phone_number(string):
    if isinstance(string, str) and string.isdigit():
        return True
    return False

def is_valid_integer(number):
    if isinstance(number, int):
        return True
    else:
        False
        
def is_valid_currency(currency):
    if isinstance(currency, float) and currency > 0:
        return True
    else:
        False

def is_valid_name_in_collection(name, collection):
    if isinstance(collection, list) and len(collection) > 0:
        try:
            filtered_list = filter(lambda x: x.name == name, collection)
            filtered_list = list(filtered_list)

            if len(filtered_list) > 0:
                print("This name is already in use")
                return False
            
            return True
        except AttributeError:
            print("Something went wrong during this operation: Attribute Error was detected")
    else:
        print("The collection is not a list or there are no items in it")
        return False
    
def is_valid_range(range_numbers):
    if isinstance(range_numbers, tuple) and len(range_numbers) == 2:
        result = True if (range_numbers[0] < range_numbers[1]) and (range_numbers[0] >= 0 and range_numbers[1] > 0) else False
        if result == False: print("Not a valid range of numbers")
        return result
    else:
        print("The range is not a tuple or doesn't contain two values")
        return False
