def is_valid_string(string):
    if isinstance(string, str) and string.isalpha():
        return True
    return False

def is_valid_phone_number(string):
    if isinstance(string, str) and string.isdecimal():
        return True
    return False

def is_valid_integer(number):
    if isinstance(number, int) and (number > 0):
        return True
    else:
        False
        
def is_valid_currency(currency):
    if isinstance(currency, float):
        return True
    else:
        False
