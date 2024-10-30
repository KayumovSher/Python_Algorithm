# c = sqrt{a^2 + b^2}

from math import sqrt

def TrianleP(a, b):
    c = sqrt((a**2)+(b**2))
    P=a+b+c
    return c, P

a = int(input("a = "))
b = int(input("b = "))

gepo, P = TrianleP(a,b)

print(f"Uchburchak:\nKatetlari - {a}, {b}\nGepotinuzasi - {gepo}\nPerimetri - {P}")