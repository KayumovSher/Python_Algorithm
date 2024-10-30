n = int(input("Enter n value (n > 1): "))

while n <= 1:
    print('Given n value must be bigger than 1. Please enter valid value!')
    n = int(input("Enter n value (n > 1): "))

# Initilize some variables
k = 1
sum_k = 0

# Ensure (1+2+3....+k)<=n or not
while sum_k <= n:
    sum_k+=k
    k+=1
    
# Output the result
print(f"The smallest integer k for which the sum is <= {n} is: {k-1}")
print(f"The sum from 1 to {k-1} is: {sum_k}")
