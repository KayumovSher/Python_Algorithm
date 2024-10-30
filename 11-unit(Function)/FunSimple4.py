# 12:24

def Triangle(x,y,z):
    P = x+y+z
    S = (x+y+z)/2
    return P, S

a = int(input("Uchburchakning A tomonini kiriting -> "))
b = int(input("Uchburchakning B tomonini kiriting -> "))
c = int(input("Uchburchakning C tomonini kiriting -> "))

Perimeter, Surface = Triangle(a,b,c)

print(f"Uchburchakning tomonlari:\nA = {a}, B = {b}, C = {c}")
print(f"Uchburchakning: Perimetri -> {Perimeter}, Yuzasi -> {Surface}")