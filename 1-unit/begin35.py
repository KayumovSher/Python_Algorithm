v1 = int(input("Qayiq tezligi km/soat da "))
v2 = int(input("Daryo oqimining tezligi kn/soat da "))

t1 = int(input("Oqim bo'ylab harakatlanish vaqti"))
t2 = int(input("Oqimga qarshi harakatlanish vaqti"))

s1 = (v1 + v2) * t1
s2 = abs(v1 - v2) * t2
print(s1)
print(s2)