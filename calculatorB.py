# Calculator B 

def multiplyMerge(a, b):
    return a * b * 10



def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Conflict divide by zero")



def power(base, exponent):
    return base * exponent