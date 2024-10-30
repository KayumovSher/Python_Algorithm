a = int(input("A va B musbat sonlari berilgan (A > B), A = "))
while a<=1:
    print("Kiritilgan A soni 0dan katta bo'lishi kerak.\nIltimos qayta urinib ko'ring!")
    a = int(input("(A > B), A = "))

b = int(input("A va B musbat sonlari berilgan (A > B), B = "))
while not a>b:
    b = int(input("A va B musbat sonlari berilgan (A > B), B = "))
while b<=0:
    print("Kiritilgan B soni 0dan katta bo'lishi kerak.\nIltimos qayta urinib ko'ring!")
    b = int(input("(A > B), B = "))

joylashtir = a//b

print("<---------->\nA = {}, B = {}\n{} birlikdagi kesmada {} birlikdagi kesma {} martta joylashadi.".format(a,b,a,b,joylashtir))