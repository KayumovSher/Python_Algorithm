x1 = int(input("1-8 oraliqda yotuvchi shaxmat doskasining x1 koordinata qiymati uchun butun son kiriting: "))
y1 = int(input("1-8 oraliqda yotuvchi shaxmat doskasining y1 koordinata qiymati uchun butun son kiriting: "))

x2 = int(input("\n1-8 oraliqda yotuvchi shaxmat doskasining x2 koordinata qiymati uchun butun son kiriting: "))
y2 = int(input("1-8 oraliqda yotuvchi shaxmat doskasining y2 koordinata qiymati uchun butun son kiriting: "))


if ((x1+y1)%2==0 and (x2+y2)%2==0) or ((x1+y1)%2!=0 and (x2+y2)%2!=0) or ((x1+y1)%2==0 and (x2+y2)%2!=0) or ((x1+y1)%2!=0 and (x2+y2)%2==0):
    print(True)
else:
    print(False)


