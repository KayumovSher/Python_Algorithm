from random import randint
m = int(input('m = '))
n = int(input('n = '))

matrix = [[randint(1,9) for i in range(m)]for j in range(n)]

for i in matrix:
    print(*i)

k = int(input('k = '))
print(matrix[k])
    
