K = int(input("1-365 gacha istalgan butun son kiriting: "))

hafta_kunlari = {
    1: 'dushanba',
    2: 'seshanba',
    3: 'chorshanba',
    4: 'payshanba',
    5: 'juma',
    6: 'shanba',
    7: 'yakshanba'
}

hafta_kuni = K%7

# x = (hafta_kuni-8)%7
x = (abs(hafta_kuni-8))%7

print(f"{K}-son haftaning {hafta_kunlari[x]} siga teng.")