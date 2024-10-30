n  = int(input("N = "))

number = 0
# degree = 1

for i in range(1, n+1):
    number += i**i
print(number)