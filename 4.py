x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

if x != y:
    if x < y:
        x1 = (x + y) / 2
    else:
        x1 = 2 * x * y

    if y < x:
        y1 = (x + y) / 2
    else:
        y1 = 2 * x * y

    print("Заміна числа x:", x1)
    print("Заміна числа y:", y1)
else:
    print("Числа x і y повинні бути різними.")
