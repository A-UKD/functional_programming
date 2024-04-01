a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

k = int(input("Введіть число k: "))

divisible_numbers = []

if a % k == 0:
    divisible_numbers.append(a)

if b % k == 0:
    divisible_numbers.append(b)

if c % k == 0:
    divisible_numbers.append(c)

if len(divisible_numbers) > 0:
    print("Числа, для яких", k, "є дільником:", divisible_numbers)
else:
    print("У чисел a, b, c немає дільників", k)
