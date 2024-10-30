a = int(input("Enter the value of a = "))
n = int(input("Enter the value of n = "))

square = 1

if n > 0:
    for i in range(1, n+1):
        square *= a**i
        
else:
    print("Value Error. N integer should be above from 0. 'n>0'")
    
print("Given value is {} and it is computed to {}. The result is {}".format(a, n, square))