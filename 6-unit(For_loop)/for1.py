k = int(input("Ixtiyoriy k uchun butun son kiriting -> "))
n = int(input("kiritgan k soningizni nechcha martta qaytarilishini n soniga kiriting (n>0)-> "))

while not n>0:
    print("n soni 0 dan katta bo'lishi kerak qayta urinib koring.")
    n = int(input("kiritgan k soningizni nechcha martta qaytarilishini n soniga kiriting (n>0)-> "))

if n>0:
    for i in range(1, n+1):
        print(f"{i}-n = {k}", )
