K = int(input("1 - 5gacha ixtiyoriy son kiriting -> "))

if 1 <= K <= 5:
    if K == 1:
        print("Yomon")
    elif K == 2:
        print("Qoniqarsiz")
    elif K == 3:
        print("Qoniqarli")
    elif K == 4:
        print("Yaxshi")
    elif K == 5:
        print("A'lo")
else:
    print("Xato")