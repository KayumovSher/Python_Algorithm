def Ishora(a):
    if a>0:
        return 1
    elif a==0:
        return 0
    elif a<0:
        return -1
    return

a = int(input("A = ")); b = int(input("B = ")); print(Ishora(a)+Ishora(b))