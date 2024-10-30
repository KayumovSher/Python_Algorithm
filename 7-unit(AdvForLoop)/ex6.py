n = int(input("N = "))

s = 0

for i in range(1, n+1):
    if n%i == 0:
        for j in range(1, i):
            s += i
        print(s)