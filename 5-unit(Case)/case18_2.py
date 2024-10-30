N = int(input("(100-999)gacha bo'lgan ixtiyoriy son kiriting -> "))

yuz = N//100
on = N%100//10
b = N%100%10
print(3)

if yuz == 1:
    print("Bir yuz ", end="")
if yuz == 2:
    print("Ikki yuz ", end="")
if yuz == 3:
    print("Uch yuz ", end="")
if yuz == 4:
    print("To'rt yuz ", end="")
if yuz == 5:
    print("Besh yuz ", end="")
if yuz == 6:
    print("Olti yuz ", end="")
if yuz == 7:
    print("Yetti yuz ", end="")
if yuz == 8:
    print("Sakkiz yuz ", end="")
if yuz == 9:
    print("To'qqiz yuz ", end="")
    
if on == 1:
    print("O'n ", end="")
if on == 2:
    print("Yigirma ", end="")
if on == 3:
    print("O'ttiz ", end="")
if on == 4:
    print("Qirq ", end="")
if on == 5:
    print("Ellik ", end="")
if on == 6:
    print("Oltmish ", end="")
if on == 7:
    print("Yetmush ", end="")
if on == 8:
    print("Sakson ", end="")
if on == 9:
    print("To'qson ", end="")
    
if b == 1:
    print("Bir", end="")
if b == 2:
    print("Ikki", end="")
if b == 3:
    print("Uch", end="")
if b == 4:
    print("To'rt", end="")
if b == 5:
    print("Besh", end="")
if b == 6:
    print("Olti", end="")
if b == 7:
    print("Yetti", end="")
if b == 8:
    print("Sakkiz", end="")
if b == 9:
    print("To'qqiz", end="")