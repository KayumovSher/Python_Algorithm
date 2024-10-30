# Given a natural number n (n > 1). Create a program that determines the largest integer k that satisfies the condition 3**k <= n.

n = int(input("Enter n value (n > 1): "))

while n <= 1:
    print("n value must be greater than 1. Please enter valid value!")
    n = int(input("Enter n value (n > 1): "))

k = 0
# action = 3**k
while 3**k <= n:
    k += 1
print(f"The largest integer k such that 3**k <= {n} is: {k - 1}")


