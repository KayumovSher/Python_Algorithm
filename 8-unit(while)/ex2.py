n = 5
for i in range(1, n+1):
    s = 0
    for j in range(1, n+1):
        if i%j == 0:
            s += 1
    if s == 2:
        print("Prime numbers from 1 to 5 ->",i)