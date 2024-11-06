from random import randint

matrix=[]
for i in range(4):
    massiv=[]
    for j in range(4):
        massiv.append(randint(1,9))
    matrix.append(massiv)
    
for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=' ')
    print()