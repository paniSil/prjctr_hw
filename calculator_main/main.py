from calculator import evaluate, convert, re_convert

print('Welcome to simple calculator! Choose numeric system to start with: \n1.Decimal (int) \n2.Decimal (float) \n3.Binary \n4.Hexadecimal')
num_system = int(input('Choose the initial numeric system (from 1 to 4): '))
x = input('Enter first number: ')
y = input('Enter second number: ')

try:
    x, y = convert(x, y, num_system)
except ValueError:
    print('You have entered wrong value. And it will not be processed properly. Try again')
    exit(1)
except TypeError:
    print('Something went wrong. Maybe you have chosen the wrong numeric system')
    exit(1)

print('These are operations you can use: \n1.Addition \n2.Substraction \n3.Division \n4.Multiplying')

try:
    z = int(input('Choose an operation (from 1 to 4): '))
    result = evaluate(x, y, z)
    print(result)
except ValueError:
    print('Please, stick to the numbers while chosing operation')
    exit(1)
except TypeError:
    print('You have not entered variables')
    exit(1)

choice = input(print('Do you want to re-convert the result? Y/N ')).strip().lower()

if choice == 'y':
    result = re_convert(result, num_system)
    print(result)
elif choice == 'n':
    print(result)
else:
    print('You\'ve entered the wrong answer')