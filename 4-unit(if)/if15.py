a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b < c:
    print(a, b)
elif a > b and c > b:
    print(a, c)
elif b > a and c > a:
    print(b, c)