a = int(input("Enter number of a = "))
b = int(input("Enter number of b = "))

square_sum = 0

if a < b:
    for i in range(a, b+1):
        square_sum += i**2
else:
    print("Error")

print("Number a = {}, number b = {} and total sum of square = {}".format(a, b, square_sum))