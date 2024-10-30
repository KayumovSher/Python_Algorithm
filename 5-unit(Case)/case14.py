from math import sqrt

# Element kiritish
element = input("Teng tomonli uchburchakning elementlari birini kiriting.\n'1'-tomoni(a), '2'-Ichki chizilgan aylana radiusi(R1), '3'-Tashqi chizilgan aylana radiusi(R2), '4'-Yuzasi(S) -> ")

# Ushbu loop orqali elementlar rostligini aniqlash
while element != '1' and element != '2' and element != '3' and element != '4':
    print("Kiritgan elementingiz raqamlarida xatolik mavjud. Iltimos qaytadan (1-4)bo'lgan raqamlarni qaytadan kiritib ko'ring!")
    element = input("Teng tomonli uchburchakning elementlari birini kiriting.\n'1'-tomoni(a), '2'-Ichki chizilgan aylana radiusi(R1), '3'-Tashqi chizilgan aylana radiusi(R2), '4'-Yuzasi(S) -> ")

# Element kiritish
num = int(input("Element miqdorini kiriting -> "))
print("Natijalar: ", end="")

# Shartli ifodadan foydalanib kiritilgan qiymatlarni aniqlash
if element == "1":
    R1 = (num*sqrt(3))/6
    R2 = 2*R1
    S = (num**2*sqrt(3))/4
    print(f"Siz ushbu {num} miqdorini Teng tomonli uchburchakning 'Tomoni' elementi uchun kiritdingiz!")
    print(f"Tomoni - {num}\nIchki chizilgan aylana radiusi - {R1}\nTashqi chizilgan aylana radiusi - {R2}\nYuzasi - {S}")

elif element == "2":
    a = 2*num*sqrt(3)
    R2 = 2*num
    S = a**2 * sqrt(3)/4
    print(f"Siz ushbu {num} miqdorini Teng tomonli uchburchakning 'Ichki chizilgan aylana radiusi' elementi uchun kiritdingiz!")
    print(f"Tomoni - {a}\nIchki chizilgan aylana radiusi - {num}\nTashqi chizilgan aylana radiusi - {R2}\nYuzasi - {S}")
    
elif element == "3":
    R1 = num/2
    a = 2*num*sqrt(3)
    S=a**2*sqrt(3)/4
    print(f"Siz ushbu {num} miqdorini Teng tomonli uchburchakning 'Tashqi chizilgan aylana radiusi' elementi uchun kiritdingiz!")
    print(f"Tomoni - {a}\nIchki chizilgan aylana radiusi - {R1}\nTashqi chizilgan aylana radiusi - {num}\nYuzasi - {S}")

elif element == "4":
    a=sqrt(3*num)/3
    R1 = (num*sqrt(3))/6
    R2 = 2*R1
    print(f"Siz ushbu {num} miqdorini Teng tomonli uchburchakning 'Yuzasi' elementi uchun kiritdingiz!")
    print(f"Tomoni - {a}\nIchki chizilgan aylana radiusi - {R1}\nTashqi chizilgan aylana radiusi - {R2}\nYuzasi - {num}")
