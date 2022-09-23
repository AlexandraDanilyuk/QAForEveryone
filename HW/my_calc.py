def sum_it(x, y):
    return x + y

def prod(x, y):
    return x*y

def div(x, y):
    try:
       return x/y
    except ZeroDivisionError:
        x = 0

def minus(x, y):
    return x - y