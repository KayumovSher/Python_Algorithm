n = int(input("n = "))

for i in range(1, n+1):
    for j in range(1, 10):
        print(i, "x", j, '=', i*j)
    print()