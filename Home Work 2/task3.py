a = int(input ("Введите цифру: "))
b = int(input ("Введите еще одну цифру: "))
print ("Результат сложения:", a + b)
print ("Результат вычитания:", a - b)
print ("Результат умножения:", a * b)
if (b == 0):
    print("Уууу, сукааа! На ноль делить нельзя")
else:
    print ("Результат деления:", a / b)
    print ("Остаток от деления:", a % b)