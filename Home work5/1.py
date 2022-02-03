a = list( map(int, input('Введите числа через пробел и нажмите Enter ').split()) )

i = a.index(max(a))
j = a.index(min(a))

a[i], a[j] = a[j], a[i]

print('Вот так вот получилось ',*a)