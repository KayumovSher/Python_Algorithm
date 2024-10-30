a = int(input("a = "))
b = int(input('b = '))
c = int(input('c = '))

if c < a:
    print("C nuqta A va B nuqta orasida yotadi")
elif c > b:
    print("C nuqta A va B nuqta orasida yotadi")
    
else:
    ac_kesma = c - a
    bc_kesma = b - c
    kopaytma = ac_kesma * bc_kesma
    print("a va c kesma uzunligi", ac_kesma)
    print("b va c kesma uzunligi", bc_kesma)
    print("kesma uzunligining ko'paytmasi", kopaytma)