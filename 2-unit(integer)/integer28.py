K = int(input("1-365 gacha ixtiyoriy butun son kiriting: "))

hafta_kunlari_soni = {
    0: '7',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6'
}

hafta_kuni = K%7

print(f"{K} soni haftaning {hafta_kunlari_soni[hafta_kuni]}-kuniga to'g'ri keladi.")