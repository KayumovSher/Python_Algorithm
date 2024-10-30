# Given a natural number n (n > 1). (1+2+3+....+k) >= n, create a program that determines the smallest number k for which the condition is fulfilled. Also display the sum from 1 to k.

# Input n variable
n = int(input('Enter n value (n > 1): '))
# Ensure n is bigger than 1 or not
while n <= 1:
    print('Given n value must be greater than 1. Please enter valid value!')
    n = int(input('Enter n value (n > 1): '))
    
# Initialize variables
k = 1
sum_k = 0

# Find the smallest k such that (1+2+3+...+k) >= n
while sum_k < n:
    sum_k += k
    k += 1
    
# Output the result
print(f"The smallest integer k for which the sum is >= {n} is: {k-1}")
print(f"The sum from 1 to {k-1} is: {sum_k}")
