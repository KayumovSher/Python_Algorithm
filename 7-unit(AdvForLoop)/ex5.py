n = int(input("N = "))

s = 0

for i in range(1, n):
    if n%i==0:
        s += i
if s == n:
    print("Mukammal")
else:
    print("Mukammal emas!")