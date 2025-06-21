def is_valid_num(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def is_invalid_num(value):

    return not is_valid_num(value)
print(is_valid_num("123"))     
print(is_valid_num("abc"))      
print(is_invalid_num("abc"))    
print(is_invalid_num(45.6))     