a = int(input("Введите число: "))
if a % 2 == 0:
    print(a,'является чётным числом')
else:
    print(a,'является нечётным числом')
if a >= 0:
    print(a,'является не отрицательным числом')
else:
    print(a,'является отрицательным числом')
if (a >= 10 and a < 100 or a <= -10 and a > -100):
    print(a,'имеет 2 цифры')
elif (a <= 9 and a >= -9):
    pass
else:
    print(a, 'имеет 3 цифры')
if (-10 < a < 10):
    print(a,'между -10 и 10')
else:
    print(a,'не между -10 и 10')
if a >= 0:
    if a % 2 == 0:
        print(a,'положительное четное число')
    else:
        print(a,'положительное нечетное число')
else:
    if a % 2 == 0:
        print(a,'отрицательное чётное число')
    else:
        print(a,'отрицательное нечётное число')


