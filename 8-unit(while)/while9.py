n = int(input("Enter value (n > 1) n = "))

while n <= 1:
    print("Given number must be greater than 1. Please enter valid number!")
    n = int(input("Enter value (n > 1) n = "))
    
k = 1
while not 3**k > n:
    k += 1
    if k == 1:
        result = 1
result = 3**k
print(f"The given value is n = {n}, the {k} degree of 3 is {result} and {result} is bigger than {n}")