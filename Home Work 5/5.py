list = [2, 3, 6, 7, 9]
print ("Наш список такой : " + str(list))
k = 1
for i in range(len(list)):
    if list[i] > k:
        index = i
        break
res = list[: i] + [k] + list[i :]
print ("А вот такой список получился : " +  str(res))