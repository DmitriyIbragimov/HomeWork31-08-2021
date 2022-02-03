list = [1,2,3,5]
print ("Наш список такой : " + str(list))
k = 999
pos = -1
for i in range(len(list)) :
                        if list[i] < k : pos = i
list = list[:pos+1] + [k] + list[pos+1:]
print ("А вот таким он получился : " +  str(list))