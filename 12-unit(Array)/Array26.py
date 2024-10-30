#Array 26

n = int(input("n = "))
a = [i for i in range(n)]
print(a)

for i in range(1,n):
    if (a[i]+a[i-1])%2!=1:
        print(i)
        break
else:
    print("Done!")