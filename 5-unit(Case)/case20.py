D = int(input("Kunni kiriting -> "))
M = int(input("Oyni kiriting -> "))

while not (D<32 and M<13):
    print("Siz kalendar hisobida bo'lmagan not'g'ri kun yoki oyni kiritdingiz. Iltimos qayta urinib ko'ring!")
    D = int(input("Kunni kiriting -> "))
    M = int(input("Oyni kiriting -> "))

if M==1:
    D//31
    if 1<=D<=19:
        print("Siznig burjingiz (Echki)")
    elif 20<=D<=31:
        print("Siznig burjingiz (Qovg'a)")
if M==2:
    D//28
    if 1<=D<=18:
        print("Siznig burjingiz (Qovg'a)")
    elif 19<=D<=28:
        print("Siznig burjingiz (Baliq)")
if M==3:
    D//31
    if 1<=D<=20:
        print("Siznig burjingiz (Baliq)")
    elif 21<=D<=31:
        print("Siznig burjingiz (Qo'y)")
if M==4:
    D//30
    if 1<=D<=19:
        print("Siznig burjingiz (Qo'y)")
    elif 20<=D<=30:
        print("Siznig burjingiz (Buzoq)")
if M==5:
    D//31
    if 1<=D<=20:
        print("Siznig burjingiz (Buzoq)")
    elif 21<=D<=31:
        print("Siznig burjingiz (Egizaklar)")
if M==6:
    D//30
    if 1<=D<=21:
        print("Siznig burjingiz (Egizaklar)")
    elif 22<=D<=30:
        print("Siznig burjingiz (Qisqichbaqa)")
if M==7:
    D//31
    if 1<=D<=22:
        print("Siznig burjingiz (Qisqichbaqa)")
    elif 23<=D<=31:
        print("Siznig burjingiz (Arslon)")
if M==8:
    D//31
    if 1<=D<=22:
        print("Siznig burjingiz (Arslon)")
    elif 23<=D<=31:
        print("Siznig burjingiz (Parizod)")
if M==9:
    D//30
    if 1<=D<=22:
        print("Siznig burjingiz (Parizod)")
    elif 23<=D<=30:
        print("Siznig burjingiz (Tarozi)")
if M==10:
    D//31
    if 1<=D<=22:
        print("Siznig burjingiz (Tarozi)")
    elif 23<=D<=31:
        print("Siznig burjingiz (Chayon)")
if M==11:
    D//30
    if 1<=D<=22:
        print("Siznig burjingiz (Chayon)")
    elif 23<=D<=30:
        print("Siznig burjingiz (O'qotar)")
if M==12:
    D//31
    if 1<=D<=21:
        print("Siznig burjingiz (O'qotar)")
    elif 22<=D<=31:
        print("Siznig burjingiz (Echki)")