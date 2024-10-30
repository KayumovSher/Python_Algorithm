from math import pi

R1 = int(input("Aylananing birinchi radiusini kiriting R1 = "))
R2 = int(input("Aylananing ikkinchi radiusini kiriting R2 = "))

while not R1 > R2:
    print("Kiritilgan birinchi Radius (R1 )qiymati ikkinchi radius (R2) qiymatidan katta bo'lishi kerak (R1 > R2).\nIltimos qaytadan kiriting.")
    R1 = int(input("Aylananing birinchi radiusini kiriting R1 = "))
    R2 = int(input("Aylananing ikkinchi radiusini kiriting R2 = "))
S1 = pi * R1 
S2 = pi * R2
S3 = pi * (R1-R2)

print("Birinchi yuza S1 = {}\nIkkinchi yuza S2 = {}\nUmumiy yuza S3 = {}".format(S1, S2, S3))
