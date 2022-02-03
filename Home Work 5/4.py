list = "123abc"
print ("Так было до удаления: " + list)
new_str = ""
for i in range(0, len(list)):
    if i != 1: #какой индекс удаляем
        new_str = new_str + list[i]
print ("Так стало после удаления : " + new_str)