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
        res = add(x, y)
        return res
    elif z == 2:
        res = substract(x, y)
        return res
    elif z == 3:
        res = divide(x, y)
        return res
    elif z == 4:
        res = multiply(x, y)
        return res

print(evaluate(2, 4, 4))
