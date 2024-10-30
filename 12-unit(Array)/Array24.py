# Array 24

n = int(input("n = "))
a = [2*i for i in range(n)]
print(a)

d = a[1] - a[0]
for i in range(2,n):
    if a[i]-a[i-1]!=d:
        print(0)
        break
else:
    print(d)