from math import pow

def PowerA3(x):
    kub = pow(x, 3)
    kub2 = x*x*x
    return kub2

a = float(input("Ixtiyoriy haqiqiy son kiriting -> a = "))
b = float(input("Ixtiyoriy haqiqiy son kiriting -> b = "))
c = float(input("Ixtiyoriy haqiqiy son kiriting -> c = "))

d = float(input("Ixtiyoriy butun son kiriting -> d = "))
e = float(input("Ixtiyoriy butun son kiriting -> e = "))

print(f"{a} ning uchinchi darajasi {PowerA3(a)}")
print(f"{b} ning uchinchi darajasi {PowerA3(b)}")
print(f"{c} ning uchinchi darajasi {PowerA3(c)}")

print(f"{d} ning uchinchi darajasi {PowerA3(d)}")
print(f"{e} ning uchinchi darajasi {PowerA3(e)}")
