a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a >= c and a >= b:
    if c >= b:
        print('Среднее число:', c)
    else:
        print('Среднее число:', b)
elif b >= a and  b >= c:
    if a >= c:
        print('Среднее число:', a)
    else:
        print('Среднее число:', c)
elif c >= a and c >= b:
    if a >= b:
        print('Среднее число:', a)
    else:
        print('Среднее число:', b)