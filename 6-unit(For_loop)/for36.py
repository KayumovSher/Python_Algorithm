n = int(input("N butun son kiriting-> "))
k = int(input("K butun son kiriting-> "))

number = 0

for i in range(1, n+1):
    number += i**k
print("N = {} butun soni va uning darajasi uchun ikkinchi K = {} butun sonlari berildi.\nShartga muvofiq kiritilingan natija : {}ga teng".format(n, k, number))