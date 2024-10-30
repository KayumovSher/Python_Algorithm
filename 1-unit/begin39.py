from math import pow, sqrt

A = int(input("Enter A value: "))
while A == 0:
    print("A value must be bigger than 0. Please enter A value, A>0")
    A = int(input("Enter A value: "))
B = int(input("Enter B value: "))
C = int(input("Enter C value: "))

D = B**2-4*A*C

if D>0:
    x1 = ((-B+sqrt(D))/(2*A))
    x2 = ((-B-sqrt(D))/(2*A))
    
    print(x1, x2)
else:
    print("Diskriminant is not bigger than 0")
    