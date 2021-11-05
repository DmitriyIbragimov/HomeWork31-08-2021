import string

n = int(input('Введи число от 1 до 52 '))
if n <=52:
    s = string.ascii_uppercase + string.ascii_lowercase
    for i in range(n):
        if i == len(s):
            break
        print(s[i], end='')
else:
    print('Говорю же от 1 до 52, а ты ввёл',n)
