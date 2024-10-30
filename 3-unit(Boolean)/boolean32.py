from math import sqrt

a = int(input("Ixtiyoriy a butun sonini kiriting: "))
b = int(input("Ixtiyoriy b butun sonini kiriting: "))
c = int(input("Ixtiyoriy c butun sonini kiriting: "))

# c = sqrt(a**2 + b**2)

if (a**2+b**2==c**2)or(b**2+c**2==a**2)or(c**2+a**2==b**2):
    print(True)
else:
    print(False)

# print(c)