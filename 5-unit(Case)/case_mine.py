# Muchallar
muchal = {
    1: "Sichqon yili",
    2: "Sigir yili",
    3: "Yo'lbars yili",
    4: "Quyon yili",
    5: "Ajdar yili",
    6: "Ilon yili",
    7: "Ot yili",
    8: "Qo'y yili",
    9: "Maymun yili",
    10: "Tovuq yili",
    11: "It yili",
    12: "To'ng'iz yili"
}

# Ranglar
color = {
    1: "Yashil",
    2: "Qizil",
}

# Burjlar
burjlar = {
    1: "Echki",
    2: "Qovg'a",
    3: "Baliq",
    4: "Qo'y",
    5: "Buzoq",
    6: "Egizaklar",
    7: "Qisqichbaqa",
    8: "Arslon",
    9: "Parizod",
    10: "Tarozi",
    11: "Chayon",
    12: "O'qotar",
}

# Input year
yil = int(input("Siz tug'ilgan yilingizni 1984-yildan boshlab keyingi 24 yillikdagi ixtiyoriy butun sonda kiriting -> "))
while not 1984<=yil<=2008:
    print("Siz shartida keltirilmagan son kiritdingiz. Iltimos qaytadan urinib ko'ring!")
    yil = int(input("Siz tug'ilgan yilingizni 1984-yildan boshlab keyingi 24 yillikdagi ixtiyoriy butun sonda kiriting -> "))

# Input month
oy = int(input("Tug'ilgan oyingizni kiritish uchun ixtiyoriy 1-12 gacha butun son kiriting -> "))
while not 1<=oy<=12:
    print("Siz shartida keltirilmagan son kiritdingiz. Iltimos qaytadan urinib ko'ring!")
    oy = int(input("Tug'ilgan oyingizni kiritish uchun ixtiyoriy 1-12 gacha butun son kiriting -> "))

# Input day
kun = int(input("Tug'ilgan kuningizni belgilagan oyning ixtiyoriy kunida kiriting ->"))
while not 1<=kun<=31:
    print("Siz shartida keltirilmagan son kiritdingiz. Iltimos qaytadan urinib ko'ring!")
    kun = int(input("Tug'ilgan kuningizni belgilagan oyning ixtiyoriy kunida kiriting ->"))

a="Sizning Tug'ilgandagi:"
# Case Yashil
if 1984<=yil<1996:
    # Leap year
    if yil==1984:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//29
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=29:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[1]}\nBurjingiz - {burjlar[1]}")
   
    if yil==1985:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[2]}\nBurjingiz - {burjlar[1]}")

    if yil==1986:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[3]}\nBurjingiz - {burjlar[1]}")

    if yil==1987:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[4]}\nBurjingiz - {burjlar[1]}")
    # Leap year
    if yil==1988:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//29
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=29:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[5]}\nBurjingiz - {burjlar[1]}")

    if yil==1989:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[6]}\nBurjingiz - {burjlar[1]}")

    if yil==1990:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[7]}\nBurjingiz - {burjlar[1]}")

    if yil==1991:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[8]}\nBurjingiz - {burjlar[1]}")
    # Leap year
    if yil==1992:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//29
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=29:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[9]}\nBurjingiz - {burjlar[1]}")

    if yil==1993:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[10]}\nBurjingiz - {burjlar[1]}")

    if yil==1994:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[11]}\nBurjingiz - {burjlar[1]}")

    if yil==1995:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[1]} {muchal[12]}\nBurjingiz - {burjlar[1]}")

# Case Qizil
if 1996<=yil<2008:
    # Leap year
    if yil==1996:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//29
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=29:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[1]}\nBurjingiz - {burjlar[1]}")
   
    if yil==1997:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[2]}\nBurjingiz - {burjlar[1]}")

    if yil==1998:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[3]}\nBurjingiz - {burjlar[1]}")

    if yil==1999:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[4]}\nBurjingiz - {burjlar[1]}")
    # Leap year
    if yil==2000:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//29
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=29:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[5]}\nBurjingiz - {burjlar[1]}")

    if yil==2001:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[6]}\nBurjingiz - {burjlar[1]}")

    if yil==2002:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[7]}\nBurjingiz - {burjlar[1]}")

    if yil==2003:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[8]}\nBurjingiz - {burjlar[1]}")
    # Leap year
    if yil==2004:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//29
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=29:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[9]}\nBurjingiz - {burjlar[1]}")

    if yil==2005:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[10]}\nBurjingiz - {burjlar[1]}")

    if yil==2006:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[11]}\nBurjingiz - {burjlar[1]}")

    if yil==2007:
        if oy==1:
            kun//31
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[1]}")
            elif 20<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[2]}")
        elif oy==2:
            kun//28
            if 1<=kun<=18:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[2]}")
            elif 19<=kun<=28:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[3]}")
        elif oy==3:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[3]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[4]}")
        elif oy==4:
            kun//30
            if 1<=kun<=19:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[4]}")
            elif 20<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[5]}")
        elif oy==5:
            kun//31
            if 1<=kun<=20:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[5]}")
            elif 21<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[6]}")
        elif oy==6:
            kun//30
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[6]}")
            elif 22<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[7]}")
        elif oy==7:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[7]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[8]}")
        elif oy==8:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[8]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[9]}")
        elif oy==9:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[9]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[10]}")
        elif oy==10:
            kun//31
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[10]}")
            elif 23<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[11]}")
        elif oy==11:
            kun//30
            if 1<=kun<=22:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[11]}")
            elif 23<=kun<=30:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[12]}")
        elif oy==12:
            kun//31
            if 1<=kun<=21:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[12]}")
            elif 22<=kun<=31:
                print(f"\n{a}\nYilingiz - {color[2]} {muchal[12]}\nBurjingiz - {burjlar[1]}")

