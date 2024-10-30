def Even(K):
    if K%2==0:
        return True
    else:
        return False
    
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print('a = ',Even(a))
print('b = ',Even(b))
print('c = ',Even(c))