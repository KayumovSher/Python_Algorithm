a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a < b and a < c or a < b == c:
    print(a)
elif b < a and b < c or b < a == c:
    print(b)
elif c < a and c < b or c < a == b:
    print(c)
elif a == b == c:
    print("Uchta son bir biri bilan teng")