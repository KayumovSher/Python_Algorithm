# n!! = n*(n-2)*(n-4)...

# Input the integer number
n = int(input("Enter number (n>0): "))

fak = 1
while n > 1:
    fak *= n
    n -= 2

print(fak)
 
