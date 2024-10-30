# The number n is given. Create an array consisting of the first n odd numbers and remove its elements.

n = int(input("Enter how many times should the odd numbers be in output: "))
massiv=[]

for i in range(n):
    # resultodd = i*2+1
    massiv.append(i*2+1)

print(massiv)

# n = int(input("Enter a number (n): "))

# # Create an array consisting of the first n odd numbers
# odd_numbers = [2*i + 1 for i in range(n)]

# # Output the array
# print(f"Array consisting of the first {n} odd numbers: {odd_numbers}")