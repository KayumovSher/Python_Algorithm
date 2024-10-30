son1 = int(input("Nolga teng bo'lmagan son kiriting -> "))
while son1==0:
    print("Kiritilgan soningiz 0ga teng bo'lmasligi kerak. Iltimos qaytadan urinib ko'ring!")
    son1 = int(input("Nolga teng bo'lmagan son kiriting -> "))

son2 = int(input("Nolga teng bo'lmagan ikkinchi sonni kiriting -> "))
while son2==0:
    print("Kiritilgan soningiz 0ga teng bo'lmasligi kerak. Iltimos qaytadan urinib ko'ring!")
    son2 = int(input("Nolga teng bo'lmagan ikkinchi sonni kiriting -> "))


print(f"Sonlarning yig'indisi: {son1} + {son2} = {son1+son2};")
print(f"Sonlarning ko'paytmasi: {son1} * {son2} = {son1*son2};")
print(f"Sonlarning moduli: {son1}, {son2} -> '|'{abs(son1)}'|' va '|'{abs(son2)}'|';")