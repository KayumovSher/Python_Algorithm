K=int(input("Istalgan musbat son kiriting (K>0): "))
while not K>0:
    print("Siz not'g'ri son kiritdingiz. Son 0 dan oshmasligi kerak!")
    K=int(input("Istalgan musbat son kiriting (K>0): "))

R=int(input("(1 <= R <= 9) iborat bo'lgan ixtiyoriy raqam kiriting: "))
while not 1<=R<=9:
    print("Siz not'g'ri son kiritdingiz. Raqam 1 dan katta va 9 dan oshmasligi kerak!")
    K=int(input("Istalgan musbat son kiriting (K>0): "))

def AddRightDigit(son, raqam):
    son = str(son); raqam = str(raqam)
    return son+raqam

print(AddRightDigit(K,R))
