n = int(input("N = "))

factorial = 1

for i in range(1, n+1):
    factorial *= i
print("The given number is {} and it's factorial = {}".format(n, factorial))