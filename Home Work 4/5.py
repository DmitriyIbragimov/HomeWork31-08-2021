from random import randint
i = randint(1,6)
from random import randint
cikl = 0
p = 0
c = int(input('Введите количество циклов '))
while cikl < c:
    i = randint(1,6)
    if (i == 3) or (i == 4):
        p = p + 1
    cikl = cikl + 1
print('Процент победы равен ', ((p/c)*100), '%')