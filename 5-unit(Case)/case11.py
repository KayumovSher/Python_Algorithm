# Lokatr dunyoning bir tomoniga qaratilgan("s"-shimol, "j"-janub, "q"-sharq, "g"-g'arb) va uchta raqamli komanda: 0-o'ngga buril, 1-chapga buril, 2-burilish 180^o.
# C - lokatrning boshlang'ich holati va K1, K2 - komandalari berilgan. Berilgan komanda bajarilgandan keyin lokatr holatini aniqlovchi dastur tuzilsin.

# Compas
#               N (Shimol)
#               |
#               |
# (G'arb)       |
# W <----------(*)----------> E 
#               |      (Sharq)
#               |
#               |
#       (Janub) S


C = input("Lokatr dunyoning qaysi tomoniga qaratilgan? ('s'-shimol, 'j'-janub, 'q'-sharq, 'g'-g'arb) -> ")
K1 = (input("'0'-o'ngga buril, '1'-chapga buril, '2'-burilish 180^o -> "))
K2 = (input("'0'-o'ngga buril, '1'-chapga buril, '2'-burilish 180^o -> "))

print("Lokatrning holati: ", end="")

if C == 's':
    if K1 == '0' and K2 == '0':
        print("Dunyoning (Janub) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '1':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '2':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
        
    elif K1 == '1' and K2 == '0':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '1':
        print("Dunyoning (Janub) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '2':
        print("Dunyoning (Sharq) tomoniga qaratilgan")

    elif K1 == '2' and K2 == '0':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '1':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '2':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
        
elif C == 'j':
    if K1 == '0' and K2 == '0':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '1':
        print("Dunyoning (Janub) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '2':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
        
    elif K1 == '1' and K2 == '0':
        print("Dunyoning (Janub) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '1':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '2':
        print("Dunyoning (G'arb) tomoniga qaratilgan")

    elif K1 == '2' and K2 == '0':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '1':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '2':
        print("Dunyoning (Janub) tomoniga qaratilgan")
        
elif C == 'q':
    if K1 == '0' and K2 == '0':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '1':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '2':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
        
    elif K1 == '1' and K2 == '0':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '1':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '2':
        print("Dunyoning (Janub) tomoniga qaratilgan")

    elif K1 == '2' and K2 == '0':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '1':
        print("Dunyoning (Janub) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '2':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
        
elif C == 'g':
    if K1 == '0' and K2 == '0':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '1':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
    elif K1 == '0' and K2 == '2':
        print("Dunyoning (Janub) tomoniga qaratilgan")
        
    elif K1 == '1' and K2 == '0':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '1':
        print("Dunyoning (Sharq) tomoniga qaratilgan")
    elif K1 == '1' and K2 == '2':
        print("Dunyoning (Shimol) tomoniga qaratilgan")

    elif K1 == '2' and K2 == '0':
        print("Dunyoning (Janub) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '1':
        print("Dunyoning (Shimol) tomoniga qaratilgan")
    elif K1 == '2' and K2 == '2':
        print("Dunyoning (G'arb) tomoniga qaratilgan")
        