a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

count_positive = 0

if a > 0:
    count_positive += 1

if b > 0:
    count_positive += 1

if c > 0:
    count_positive += 1

print("Кількість додатніх чисел:", count_positive)
