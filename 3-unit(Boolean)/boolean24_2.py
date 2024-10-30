from math import *

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b**2 - 4*a*c
x = (-b+sqrt(D))/(2*a)
print(a * x**2 + b * x + c == 0)