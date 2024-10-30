a = int(input("Paralepipedning a tomonini kiriting -> "))
b = int(input("Paralepipedning b tomonini kiriting -> "))
c = int(input("Paralepipedning c tomonini kiriting -> "))

# Hajmini topish formulasi
V = a * b * c
# To'la sirtini topish formulasi
S = 2 * (a * b + b * c + a * c)

print("Paralepipedning hajmi V = {} ga to'la sirti S = {} ga teng".format(V, S))