

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
print(is_number("-2"))    # True
print(is_number("-4.7"))  # True
print(is_number("abc"))   # False