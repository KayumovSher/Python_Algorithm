K = int(input("1-365 gacha bo'lgan ixtiyoriy butun son kiriting: "))

hafta_kunlari = {
    1: 'dushanba',
    2: 'seshanba',
    3: 'chorshanba',
    4: 'payshanba',
    5: 'juma',
    6: 'shanba',
    7: 'yakshanba',
}

hafta = K%7

x = hafta+1

print(f"{K} soni haftaning {hafta_kunlari[x]} kuniga to'g'ri keladi.")