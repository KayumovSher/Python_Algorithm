# Array 27
from random import randint

n = int(input("n = "))
a = [randint(-5,5) for i in range(n)]
print(a)

for i in range(1,n):
    if a[i]*a[i-1]>0:
        print(i)
        break
else:
    print("Done!")``