a = int(input("Enter a = "))
b = int(input("Enter b = "))

total_num = 1
if a < b:
    for i in range(a, b+1):
        total_num *= i
    print("Number a = {}, number b = {} and the product of two numbers = {}".format(a, b, total_num))
else:
    print("Error")
    
