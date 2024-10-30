from math import *

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a != 0:
    D = pow(b, 2) - 4*a*c
    # print(D)
    if D > 0:
        x1 = (-b + sqrt(D))/(2*a)
        print(x1); print(a*pow(x1, 2) + b*x1 + c == 0)
        x2 = (-b - sqrt(D))/(2*a)
        print(x2); print(a*pow(x2, 2) + b*x2 + c == 0)
    elif D == 0:
        x = -b/(2*a)
        print(a*pow(x, 2) + b*x + c == 0)
    else:
        print("Ildiz Yechimga ega emas.")
        
else:
    print("a soni noldan farqli.")
        
    
    