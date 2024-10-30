from math import sqrt, pow

a  = int(input("To'g'ri to'rtburchakning katetini kiriting a = "))
b  = int(input("To'g'ri to'rtburchakning katetini kiriting b = "))

c = sqrt(pow(a, 2) + pow(b, 2))

P = a + b + c

print("To'g'ri to'rtburchaklarning katetlari: a = {}, b = {};\nUlarning Gipotenuzasi: c = {};\nUlarning Perimetri: P = {};".format(a,b,c,P))