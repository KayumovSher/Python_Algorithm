son = int(input("1 - 7 gacha son kiriting -> "))

if 1 <= son <= 7:
    if son == 1:
        print("Dushanba")
    elif son == 2:
        print("Seshanba")
    elif son == 3:
        print("Chorshanba")
    elif son == 4:
        print("Payshanba")
    elif son == 5:
        print("Juma")
    elif son == 6:
        print("Shanba")
    elif son == 7:
        print("Yakshanba")
else:
    print("Iltimos 1 dan 7 gacha son kliriting")