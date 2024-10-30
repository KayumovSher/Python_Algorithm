n = int(input("Vertikal ko'paytirish jadvali uchun ixtiyoriy 1-10 gacha butun son kiriting -> "))

for i in range(1, n+1):
    for j in range(1, 11):
        print(i,'X',j,'=', i*j, end='\n')
    print()