a = int(input("Введите целое число до 15: "))
if a>15:
    print('Вы ввели большое число')
else:
    y = bin(a)
    new = y.replace("b", "")
    print(a,"Ваше число в двоичном формате : ", new)