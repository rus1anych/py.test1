import math
com = input()
if com == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)
elif com == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a*b
    print(S)
elif com == 'круг':
    r = float(input())
    pi = 3.14
    S = pi*r**2
    print(S)
else:
    print('нет такого варианта')