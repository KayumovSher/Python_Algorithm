V1 = int(input("Birinchi avtomobil tezligini kiriting - "))
V2 = int(input("Ikkinchi avtomobil tezligini kiriting - "))
S = int(input("Ular orasidagi masofani kiriting - "))
T = int(input("Vaqtni kiriting - "))

distance1 = V1 * T
distance2 = V2 * T
total_distance = S - (V1 + V2)
print("Ular orasidagi masofa {}km bo'lgan ikki avtomobil bir-biri tomonga {}km/soat va {}km/soat tezlik bilan {}soat harakatlanishdi, ular orasida {}km masofa qoldi.".format(S, V1, V2, T, total_distance))