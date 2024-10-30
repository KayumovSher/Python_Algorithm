a = int(input("Istalgan musbat sonini kiriting A = "))
b = int(input("Istalgan A dan kichik bo'lgan musbat sonini kiriting (A>B) -> "))

while not a>b:
    print("Kiritgan B qiymatingiz A qiymatidan kichik bo'lishi kerak. Iltimos qayta urinib ko'ring!")
    
    b = float(input("Istalgan A dan kichik bo'lgan musbat sonini kiriting (A>B) -> "))


if a>0 and b>0:
    while a>b:
        a-=b
    print(f"A uzunlikdagi kesmada maksimal darajada B kesmaga joylashtirilgandan so'ng A kesmaning bo'sh qisminig javobi = {a}")

else:
    print("A yoki B ning qiymati 0ga teng iltimos ushbu algoritmni qayta ishga tushiring.")
