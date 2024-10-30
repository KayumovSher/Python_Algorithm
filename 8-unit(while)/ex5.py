n = int(input("n = "))


# Initialize the divisor and divisors list
divisor = 1
divisors = []

# Find divisors using a while loop
while divisor <= n:
    if n % divisor == 0:
        divisors.append(divisor)
    divisor += 1

# Print the result
print(f"The divisors of {n} are: {divisors}")