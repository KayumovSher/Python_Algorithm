n = int(input("n = "))

for i in range(1, n+1):
    s = 0
    for j in range(1, i+1):
        if i%j ==0:
            s+=1
    if s == 2:
        last = i
    # print(i)
        
for j in range(1, n+1):
    s = 0
    for k in range(1, i+1):
        if j%k ==0:
            s+=1
    if s == 2:
        print(j)
        break
    
print("The given number is {}. {} and {}.".format(n, j, i))