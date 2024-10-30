n = int(input("N = "))

for i in range(1, n+1):
    s = 0
    for j in range(1, i+1):
        if i%j == 0:
            s += 1
    if s%2==0 and s>2:
        # last = i
        print(i)
    # elif s%3==0:
    #     continue
        