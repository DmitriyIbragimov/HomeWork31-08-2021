list = [14, 88, 13, 7, 94, 51, 22]
it = iter(list)
del list[2]
for x in it:
    print(x, end=' ')
