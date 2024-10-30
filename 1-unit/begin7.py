from math import pow, pi

R = int(input("Aylananing radiusini kiriting R = "))

L = 2 * pi * R
S = pi * pow(R, 2)

print("Aylananing uzunligi L = {} va To'la sirti S = {} ga teng.".format(L, S))