a = int(input("a = "))
s = 0
while a!=0:
    if a%10==2:
        s+=1
    a//=10
    
print(s)