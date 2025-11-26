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
