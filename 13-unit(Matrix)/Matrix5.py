from random import randint

m = int(input('m = '))
n = int(input('n = '))

d = int(input('d = '))

massiv_nm = [randint(1,9) for i in range(m)]
matrix=[]
for i in range(m):
    massiv = [massiv_nm[i]]
    for j in range(1,n):
        massiv.append(massiv[j-1]+d)
    matrix.append(massiv)
    
# print(matrix)

for i in matrix:
    print(*i)