from math import sqrt

a = int(input("Manfiy bo'lmagan ixtiyoring butun son kiriting a -> "))
while not a>0:
    print("Kiritilgan son 0 dan katta bo'lishi shart. Iltimos qaytadan urinib ko'ring")
    a = int(input("Manfiy bo'lmagan ixtiyoring butun son kiriting a -> "))

b = int(input("Manfiy bo'lmagan ixtiyoring butun son kiriting b -> "))
while not b>0:
    print("Kiritilgan son 0 dan katta bo'lishi shart. Iltimos qaytadan urinib ko'ring")
    b = int(input("Manfiy bo'lmagan ixtiyoring butun son kiriting b -> "))

root = sqrt(a * b)
print(f"Kiritilgan sonning o'rta arifmetigi {root} ga teng.")
