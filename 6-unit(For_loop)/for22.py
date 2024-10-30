x = int(input("Enter the value of x = "))
n = int(input("Enter the degree for x and the denominator.\nEnter the degree & denominator of n = "))

degree = 0


if n > 0:
    for i in range(1, n+1):
        degree += (x ** i) / i
    print("The given value is {}, degree & denominator num is {} and result is {}".format(x, n, degree))

else:
    print("Value error - n>0")