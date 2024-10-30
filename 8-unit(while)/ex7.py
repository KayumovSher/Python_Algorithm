n = int(input("n = "))

if n%2==0:
    n-=1
while n>=1:
    print(n, end=' ')
    n-=2
