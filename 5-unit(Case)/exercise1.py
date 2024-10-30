# 0 dan 55 gacha yigildi 56dan 70gacha 3 71 dan 85gacha 4 86 dan 100 gacha 5

ball = int(input("Ball - "))

if ball > 0 and ball <= 100:
    if ball >= 1 and ball <= 55:
        print("2 baho")
    elif ball >= 56 and ball <= 70:
        print("3 baho")
    elif ball >= 71 and ball <= 85:
        print("4 baho")
    elif ball >= 86 and ball <= 100:
        print("5 baho")
else:
    print("Iltimos 0 dan 100 gacha to'plagan balingizni kiriting")