list = ['q', 'x', 'ы','R' , 'л', 'j', 'y', 'Q', ' ', ' ', '.', '.']
stroka = ""
for i in list:
            if ord(i) in range(97, 122) or ord(i) in range(65, 90) or ord(i) == 46 or ord(i) == 32:
                                                                                                    stroka += i
print(stroka)