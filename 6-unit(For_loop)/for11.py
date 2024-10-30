# S = n**2 + (n+1)**2 + (n+2)**2 + ....(2*n)**2

n = int(input("Enter n = "))

number = 0

if n > 0:
    for i in range(n, 2*n + 1):
        number += i**2
else:
    print("Value error")
    
print("The given number is n = {} and the sum is = {}".format(n, number))