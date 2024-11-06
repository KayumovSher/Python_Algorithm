from random import randint

matrix = [[randint(1,9) for i in range(4)]for j in range(4)]

for i in matrix:
    print(*i)