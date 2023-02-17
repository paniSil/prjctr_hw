from bases import Bases

def convert(x: str, y: str, num_system: int):
    if num_system == 1:  # Decimal (int)
        x = int(x)
        y = int(y)
        return x, y
    elif num_system == 2: # Decimal (float)
        x = float(x)
        y = float(y)
        return x, y
    elif num_system == 3: # Binary
        bases = Bases()
        x = bases.fromBase2(str(x))
        y = bases.fromBase2(str(y))
        return x, y
    elif num_system == 4: # Hexadecimal
        bases = Bases()
        x = bases.fromBase16(x)
        y = bases.fromBase16(y)
        return x, y
    else:
        print('You\'ve chosen the wrong operation')

def re_convert(res, num_system):
    if num_system == 3: # Binary
        bases = Bases()
        res = bases.toBase2(res)
        return res
    elif num_system == 4: # Hexadecimal
        bases = Bases()
        res = bases.toBase16(res)
        return res
    elif num_system == 1 or 2:
        print('Your starting input suggested that you do not need re-conversion. Your result is: ', res)
    else:
        ('Probably this error would occur earlier but basically your initial system choice was wrong')
        

#print(re_convert(5676, 3))