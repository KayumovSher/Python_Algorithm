a =  int(input('a = '))
b =  int(input('b = '))
c =  int(input('c = '))


if b > a < c or a < b == c:
    kichik_1 = a
    print(kichik_1)
    # if b < a > c or a > b == c:
    #     print(a)
elif a > b < c or b < a == c:
    kichik_2 = b
    print(kichik_2)
elif a > c < b or c < a == b:
    kichik_3 = c
    print(kichik_3)
    
elif c > a == b:
    ikki_kichik = a or b
    print(ikki_kichik)
elif a > b == c:
    ikki_kichik = b or c
    print(ikki_kichik)
elif b > a == c:
    ikki_kichik = a or c
    print(ikki_kichik)
    
    
if b < a > c or a > b == c:
    katta_1 = a
    print(katta_1)
    # if b < a > c or a > b == c:
    #     print(a)
elif a < b > c or b > a == c:
    katta_2 = b
    print(katta_2)
elif a < c > b or c > a == b:
    katta_3 = c
    print(katta_3)
    
elif c < a == b:
    ikki_katta = a or b
    print(ikki_katta)
elif a < b == c:
    ikki_katta = b or c
    print(ikki_katta)
elif b < a == c:
    ikki_katta = a or c
    print(ikki_katta)
elif a == b == c:
    print("siz uch xil butun son kiritishingiz kerak")