m = int(input('m = '))
n = int(input('n = '))

matrix = []
for i in range(m):
    massiv = []
    for j in range(n):
        massiv.append(i++1)
    matrix.append(massiv)
    
for i in matrix:
    print(*i)
    