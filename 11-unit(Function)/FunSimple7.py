a = int(input("Raqamni kiriting: "))
b = int(input("Raqamni kiriting: "))
c = int(input("Raqamni kiriting: "))

def InvertDigit(x):
    teskari_tartib = 0  # Teskari tartibda raqamlarni saqlash uchun

    while x > 0:
        raqam = x % 10  # Raqamni olish
        teskari_tartib = teskari_tartib * 10 + raqam  # Raqamni teskari tartibda qo'shish
        x //= 10  # Raqamni o'chirish
    return teskari_tartib

print(f"1 - Raqam = {a}, Teskari tartibda: {InvertDigit(a)}")
print(f"2 - Raqam = {b}, Teskari tartibda: {InvertDigit(b)}")
print(f"3 - Raqam = {c}, Teskari tartibda: {InvertDigit(c)}")