n = int(input("Karta qiymatini 6 dan 14gacha ixtiyoriy birini kiriting;\n6 da 10 gacha oddiy raqamlar va 11 dan 14 gacha - 11(Valet), 12(Dama), 13(Karol), 14(Tuz) ketma ketlikda. -> "))

while n < 6 or n > 14:
    print("Karta qiymatini to'gri kiritmadingiz iltimos qaytadan (6-14) raqamlaridan birini tanlang!") 
    n = int(input("Karta qiymatini 6 dan 14gacha ixtiyoriy birini kiriting;\n6 da 10 gacha oddiy raqamlar va 11 dan 14 gacha - 11(Valet), 12(Dama), 13(Karol), 14(Tuz) ketma ketlikda. -> "))
    
m = int(input("Karta turini 1dan 4agacha ixtiyoriy birini kiriting;\n1(G'isht), 2(Olma), 3(Chillik), 4(Qarg'a). -> "))

while m < 1 or m > 4:
    print("Karta turini to'g'ri kiritmadingiz. Iltimos (1-4) raqamlardan birini qaytadan tanlang!")
    m = int(input("Karta turini 1dan 4agacha ixtiyoriy birini kiriting;\n1(G'isht), 2(Olma), 3(Chillik), 4(Qarg'a). -> "))

if 6 <= n <= 14 and 1 <= m <= 4:
    if n == 6:
        if m == 1:
            print("Olti G'isht")
        elif m == 2:
            print("Olti Olma")
        elif m == 3:
            print("Olti Chillik")
        elif m == 4:
            print("Olti Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 7:
        if m == 1:
            print("Yetti G'isht")
        elif m == 2:
            print("Yetti Olma")
        elif m == 3:
            print("Yetti Chillik")
        elif m == 4:
            print("Yetti Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 8:
        if m == 1:
            print("Sakkiz G'isht")
        elif m == 2:
            print("Sakkiz Olma")
        elif m == 3:
            print("Sakkiz Chillik")
        elif m == 4:
            print("Sakkiz Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 9:
        if m == 1:
            print("To'qqiz G'isht")
        elif m == 2:
            print("To'qqiz Olma")
        elif m == 3:
            print("To'qqiz Chillik")
        elif m == 4:
            print("To'qqiz Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 10:
        if m == 1:
            print("O'n G'isht")
        elif m == 2:
            print("O'n Olma")
        elif m == 3:
            print("O'n Chillik")
        elif m == 4:
            print("O'n Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 11:
        if m == 1:
            print("Valet G'isht")
        elif m == 2:
            print("Valet Olma")
        elif m == 3:
            print("Valet Chillik")
        elif m == 4:
            print("Valet Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 12:
        if m == 1:
            print("Dama G'isht")
        elif m == 2:
            print("Dama Olma")
        elif m == 3:
            print("Dama Chillik")
        elif m == 4:
            print("Dama Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 13:
        if m == 1:
            print("Karol G'isht")
        elif m == 2:
            print("Karol Olma")
        elif m == 3:
            print("Karol Chillik")
        elif m == 4:
            print("Karol Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")
    elif n == 14:
        if m == 1:
            print("Tuz G'isht")
        elif m == 2:
            print("Tuz Olma")
        elif m == 3:
            print("Tuz Chillik")
        elif m == 4:
            print("Tuz Qarg'a")
        else:
            print("Siz karta turini kiritmadingiz! Qayta urinib ko'ring")   
else:
    print("Noto'g'ri qiymat yoki karta turini kiritdingiz iltimos qaytadan urinib ko'ring!")