def is_valid_string(string):
    if isinstance(string, str) and string.isalnum():
        return True
    return False

def is_valid_text(text):
    if isinstance(text, str):
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
