from random import randint

m = int(input('m = '))
n = int(input('n = '))

massiv = [randint(1,9) for i in range(n)]
print(massiv)
matrix = []
for i in range(m):
    matrix.append(massiv)

for i in matrix:
    print(*i)
