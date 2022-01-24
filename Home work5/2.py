import re
r = re.compile("[a-zA-Z .]+")
list = ['Ф', 'cat', 'Fuck', '...', 'Приветики', '  ', 'hehe','Куа']
print('Наш массив символов выглядит так: ', list)
list1 = [w for w in filter(r.findall, list)]
print('Наш выбранный массив вот такой: ', " ".join(list1))