n = int(input("Enter n value (n > 0): "))
# Ensure n is bigger than 0 or not
while n<=0:
    print("n value must be bigger than 0. Enter valud number!")
    n = int(input("Enter n value (n > 0): "))
k = 0
while (k+1)**2<=n:
    k += 1
result = k**2
print(f"Given value n = {n}, k = {k} and {result}is not bigger than {n} ")