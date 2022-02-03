a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
b = ['a', 'b', 'c', 'g', 'w']
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break
print(c)

# По нему уже стоит зачёт