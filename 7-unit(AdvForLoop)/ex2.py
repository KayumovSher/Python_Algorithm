n = int(input("Enter N() value: N = "))
k = int(input("Enter K() value: K = "))

number = 0

for i in range(1, n+1):
    number += i/(k**5)
print(number)