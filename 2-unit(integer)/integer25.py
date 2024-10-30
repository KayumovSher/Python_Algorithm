K = int(input("1dan 365 gacha bo'lgan ixtiyoriy son kiriting! K = "))



hafta_kunlari = {
    0: 'yakshanba',
    1: 'dushanba',
    2: 'seshanba',
    3: 'chorshanba',
    4: 'payshanba',
    5: 'juma',
    6: 'shanba'
}

hafta = K%7
payshanba = (hafta+3) % 7

print(f"{K}-kun haftaning {hafta_kunlari[payshanba]} kuniga to'g'ri keladi.")