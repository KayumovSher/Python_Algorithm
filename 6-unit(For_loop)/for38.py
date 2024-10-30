n = int(input("N = "))

number = 0

for i in range(1, n+1):
    number += i**(n-i+1)
print(number)