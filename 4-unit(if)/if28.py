year = int(input("Yil kiriting(Musbat butun son) -> "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"Kiritilgan {year}, kabisa yili.")
else:
    print(f"Kiritilgan {year}, kabisa yili emas")

