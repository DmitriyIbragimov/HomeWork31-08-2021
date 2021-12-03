n = int(input('Введи число от 1 до 52 '))
m = range(65,65+n)
if n <=52:
    for i in m:
        if i > 90:
            print(chr(i + 6), end = '')
        else:
            print(chr(i), end = '')
else:
    print('Говорю же от 1 до 52, а ты ввёл',n)