# # S = 1.1*1.2*1.3*....n

# n = int(input("Enter n = "))

# number = 1

# if n > 0:
#     for i in range(n+1):
#         number *= i/10

# else:
#     print("Error")
# print(number)


# Input the value of n
n = int(input("Enter the value of n: "))

# Initialize the product variable
series_product = 1.0  # Start with 1.0 to store the product of the series

# Calculate the product of the series
for i in range(1, n + 1):
    series_product *= 1.1 * i
    # print("The product of the series is:", series_product)

# Output the result
print("The product of the series is:", series_product)
