from math import sqrt

def IsSquare(K):
    if K>0:
        kvad_ildiz = sqrt(K)
        if kvad_ildiz == int(kvad_ildiz):
            return True
        else:
            return False
            
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print('a = ', IsSquare(a))
print('b = ', IsSquare(b))
print('c = ', IsSquare(c))
 