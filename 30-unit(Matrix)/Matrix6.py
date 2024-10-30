from random import randint

m = int(input('m = '))
n = int(input('n = '))

q = int(input('q = '))

massiv_nm = [randint(1,9) for i in range(m)]

matrix = []
for i in range(m):
    massiv = [massiv_nm[i]]
    for j in range(1,n):
        massiv.append(massiv[j-1]*q)
    matrix.append(massiv)
    
for i in matrix:
    print(*i)
        