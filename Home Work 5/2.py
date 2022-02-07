list = ['q', 'x', 'ы','R' , 'л', 'j', 'y', 'Q', ' ', ' ', '.', '.']
stroka = ""
for i in list:
            if ( 'a'< i and i<'z') or ('A'< i and i<'Z') or (i == '.') or (i == ' '):
                                                                                    stroka += i
print(stroka)