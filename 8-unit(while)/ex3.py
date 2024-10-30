i = 1; j = 1 
while i <= 5:
    s = 0
    for k in range(1, j+1):
        if j%k == 0:
            s+=1
    if s==2:
        print("Prime number ->",j)
        i+=1
    j+=1