def evaluate(x: int, y:int, z):
    if z == 1:
        result = x + y
        return result        
    elif z == 2:
        result = x - y
        return result        
    elif z == 3:
        if y != 0:
            result = x / y
            return result            
        else:
            print('Zero can\'t be a divider')
    elif z == 4:
        result = x * y
        return result
    else:
        print('You\'ve chosen the wrong operation')
        exit(1)


#print(evaluate(2, 2, 4))