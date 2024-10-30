n = int(input("Enter the number of n = "))

number = 1

if n > 0:
    for i in range(1, n+1):
        number *= i
    print("Given value is {} and the result is {}.".format(n, number))
else:
    print("Value n > 0 error")