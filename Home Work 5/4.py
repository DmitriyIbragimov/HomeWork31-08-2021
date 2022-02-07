list1 = ["123abc"]
listtostr = ''.join(list1)
print ("Так было до удаления: " + listtostr)
new_str = ""
a = 2 #тут указываем, какой индекс удалить
for i in range(0, len(listtostr)):
    if i != a:
        new_str = new_str + listtostr[i]
print ("Так стало после удаления : " + new_str)