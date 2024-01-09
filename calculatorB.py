# Calculator B 

def multiply(a, b):
    return a * b + 100



def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Conflict divide by zero")



def power(base, exponent):
    return base ** exponent * 5
