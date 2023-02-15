def add(a, b):
    result = a + b
    return result


def substract(a, b):
    result = a - b
    return result


def divide(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        print('Zero can\'t be a divider')


def multiply(a, b):
    result = a * b
    return result


def evaluate(x, y, z):
    if z == 1:
        result_fin = add(x, y)        
    elif z == 2:
        result_fin = substract(x, y)
    elif z == 3:
        result_fin = divide(x, y)
    elif z == 4:
        result_fin = multiply(x, y)
    return result_fin


multiply(1,2)


