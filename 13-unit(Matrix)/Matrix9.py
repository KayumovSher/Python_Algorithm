from random import randint

m = int(input('m = '))
n = int(input('n = '))

print()

matrix = [[randint(1,9) for i in range(m)]for j in range(n)]

for i in matrix:
    print(*i)
    
print()
    
for i in range(len(matrix)):
    for j in range(0, len(matrix[0]),2):
        print(matrix[i][j], end=' ')
    print()