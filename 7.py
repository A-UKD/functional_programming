a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

count_negative = 0

if a < 0:
    count_negative += 1

if b < 0:
    count_negative += 1

if c < 0:
    count_negative += 1

print("Кількість негативних чисел:", count_negative)
