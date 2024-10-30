n = int(input("Enter the value of n = "))

number = 0

if n > 0:
    for i in range(1, n+1):
        number += i
    print("Given number is n = {} and the result is result = {}".format(n, number))
else:
    print("Value Error n > 0")