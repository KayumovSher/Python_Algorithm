a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a < b < c:
    a = 2 * a
    b = 2 * b
    c = 2 * c
else:
    a = -a
    b = -b
    c = -c
print(a,b,c)