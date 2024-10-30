n = int(input('0 dan yuqori bo\'lgan ixtiyoriy N sonini kiriting. N = '))
while not n>0:
    print("Siz 0ga teng yoki 0dan kichik bo'lgan son kiritdizgiz. Iltimos shartini diqqat bilan o'qib qaytadan urinib ko'ring!")
    n = int(input('0 dan yuqori bo\'lgan ixtiyoriy N sonini kiriting. N = '))
 
a = [i for i in range(n)]
print(a)

k = int(input('Kiritgan N ta raqamingizdan yuqori bo\'lmagan ixtiyoriy K sonini kiriting. K = '))
l = int(input('Kiritgan N ta raqamingizdan yuqori bo\'lmagan ixtiyoriy L sonini kiriting. L = '))

yigindi = sum(range(k, l+1))

print(yigindi)