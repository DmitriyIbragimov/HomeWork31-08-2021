n = int(input('Введите число от 1 до 100 '))
if n <=100:
    for i in range(1,n+1):
        for j in range(1, i+1):
           print(i, end="")
        print()
else:
    print('Говорю же, от 1 до 100, а ты ввел',n)