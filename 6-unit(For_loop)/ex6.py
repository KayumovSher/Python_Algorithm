n = int(input("N = "))

for i in range(n):
    for j in range(i, 0, -1):
        print(j, end=' ')
    for j in range(0, n-i):
        print(j, end=' ')
    print()
