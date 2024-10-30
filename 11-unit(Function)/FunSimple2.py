from math import pow
def PowerA234(x, y, z):
    pow2 = pow(x,2)
    pow3 = pow(y,3)
    pow4 = pow(z,4)
    return pow2, pow3, pow4

A = int(input("Ixtiyoriy haqiqiy son kiriting -> A = "))
B = int(input("Ixtiyoriy haqiqiy son kiriting -> B = "))
C = int(input("Ixtiyoriy haqiqiy son kiriting -> C = "))

power2A, power3A, power4A = PowerA234(A, A, A)
power2B, power3B, power4B = PowerA234(B, B, B)
power2C, power3C, power4C = PowerA234(C, C, C)

print(f"{A} ning 2-darajasi -> {power2A}, 3-darajasi -> {power3A}, 4-darajasi -> {power4A}")
print(f"{B} ning 2-darajasi -> {power2B}, 3-darajasi -> {power3B}, 4-darajasi -> {power4B}")
print(f"{C} ning 2-darajasi -> {power2C}, 3-darajasi -> {power3C}, 4-darajasi -> {power4C}")
