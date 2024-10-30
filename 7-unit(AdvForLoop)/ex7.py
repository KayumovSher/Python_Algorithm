n = int(input("N = "))

num = 0

for i in range(1, n+1):
    if n%i == 0:
        num += 1
print(num)