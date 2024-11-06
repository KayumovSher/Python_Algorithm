from random import randint

matrix = [[randint(1,9)for i in range(4)]for j in range(4)]

for i in matrix:
    print(*i)
matrix[0].pop(3)
print(matrix)
matrix[1].insert(3,15)

print(len(matrix))
print(len(matrix[0]))