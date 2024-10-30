a = int(input("Ixtiyoring 1 dan katta bo'lgan butun son kiriting a -> "))
while not a>1:
    print("Siz noto'g'ri qiymat kiritdingiz kiritilishi kerak bo'lgan qiyman 1dan katta bo'lishi kerak. Iltimos qayta urinib ko'ring!")
    a = int(input("Ixtiyoring 1 dan katta bo'lgan butun son kiriting a -> "))

k = 1
while k>=a:
    sumf = 1+1/k
    k+=1

print(f"a={a}")