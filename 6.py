a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

if a != b:
    max_num = max(a, b)

    a = max_num
    b = max_num
else:
    a = 0
    b = 0

print("Заміна числа a:", a)
print("Заміна числа b:", b)
