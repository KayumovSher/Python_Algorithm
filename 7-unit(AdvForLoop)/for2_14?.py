N=int(input("Ixtiyoriy musbat son (N>0) kiriting ->"))

while not N>0:
    print("Siz berilgan shartdan tashqari bo'lgan qiymat kiritdingiz, Iltimoss qaytadan kiriting!")
    N=int(input("Ixtiyoriy musbat son (N>0) kiriting ->"))

# S=0

for i in range(1, N+1):
    if i%2!=0:
        i+=1
    print(i, end=' ')