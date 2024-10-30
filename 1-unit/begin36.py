v1 = int(input("Birinchi avtomobil tezligi(V1) - "))
v2 = int(input("Ikkinchi avtomobil tezligi(V2) - "))
s = int(input("Masofa wiriting(S) - "))
t = int(input("Vaqtni(t) wiriting - "))

distance_car1 = v1 * t
distance_car2 = v2 * t

total_distance = s + distance_car1 + distance_car2

print("Uar {}soat vaqtda {}km masofani bosib o'tishdi.".format(t, total_distance))

