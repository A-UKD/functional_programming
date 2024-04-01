a = int(input())
b = int(input())
c = int(input())

if a < 0:
    a = a ** 4
else:
    a = a ** 2

if b < 0:
    b = b ** 4
else:
    b = b ** 2

if c < 0:
    c = c ** 4
else:
    c = c ** 2

print(a, b, c)
