from calculator.evaluation import add, substract, divide, multiply, evaluate

print('These are operations you can use: \n1.Addition \n2.Substraction \n3.Division \n4.Multiplying')
z = input('Choose an operation (1, 2, 3, 4) ')
x = input('Enter first number ')
y = input('Enter second number ')

print(evaluate(x, y, z))