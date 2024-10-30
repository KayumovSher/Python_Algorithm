n = int(input('n = '))

# s = 1

for i in range(1, n+1):
    print(' '*(n-i), end=' ')
    for j in range(i):
        print(i, end=' ')
    print()