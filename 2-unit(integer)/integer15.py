n = int(input("Ixtiyoriy uch xonalik butun son kiriting:"))
while n<=99 or n>999:
    print("Siz uch xonalik butun sondan kam yoki ko'p son kiritdizgiz.")
    n = int(input("Iltimos ixtiyoriy uch xonalik butun son kiriting:"))
else:
    yuzlik = n//100
    onlik = n//10%10
    birlik = n%10%10

    change_yuz = onlik
    change_on = yuzlik

    yuzlik = change_yuz
    onlik = change_on

    print(str(yuzlik) + str(onlik)+str(birlik))