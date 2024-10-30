
# 1 + a + a**2 + a**3 .... + a**n
a = int(input("Enter the value of a = "))
n = int(input("Enter the value of n = "))

number = 0

if n > 0:
    for i in range(n+1):
       number += a**i
    print("Given value is {} and it is computed to {}.\nThe result is {}".format(a, n, number))
else:
    print("Value Error 'n>0'")
    
