n = int(input("Enter n value (n > 0): "))
# Ensure n is bigger than 0 or not
while n<=0:
    print("n value must be bigger than 0. Enter valud number!")
    # Input again to determine n value 
    n = int(input("Enter n value (n > 0): "))
k = 1
# Ensure 2 power of k = 1 variable is bigger than n value or not
while not k**2>n:
    # if the condition is true k should be added to 1
    k += 1
# To output the action is added
result = k**2
print(f"Given number is {n} and  (k**2 > n) second number is {k}, the power of k = {result} is bigger than {n}")