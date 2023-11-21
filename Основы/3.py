import math
a = float(input())
b = float(input())
operator = input()
if operator == '+':
    print (a + b)
elif operator == '-':
    print (a - b)
elif operator == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
if operator == '*':
    print(a * b)
elif operator == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif operator == 'pow':
    print(a ** b)
elif operator == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')

