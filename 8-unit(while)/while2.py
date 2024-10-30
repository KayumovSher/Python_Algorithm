a = int(input("Butun musbat son kiriting A -> "))
b = int(input("B butun musbat son kiriting va A dan kichik bo'lsin (A>B) -> "))

while not a>b:
    print("Kiritilgan B qiymat A qiymatdan kichik bo'lishi kerak. Iltimos qayta urinib ko'ring!")
    b = int(input("B butun musbat son kiriting va A dan kichik bo'lsin (A>B) -> "))

a2=a
count = 0
while a>b:
    a-=b
    count += 1
print(f"Kiritgan qiymatlaringiz\nA = {a2}, B = {b},\nA kesmada B kesmani {count}ta joylashtirish mumkin. ")

