a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

count_integer = 0

if a.is_integer():
    count_integer += 1

if b.is_integer():
    count_integer += 1

if c.is_integer():
    count_integer += 1

print("Кількість цілих чисел:", count_integer)
