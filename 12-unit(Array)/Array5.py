n = int(input("n = "))

fib = [0,1]

for i in range(2, n):
    fib.append(fib[i-1]+fib[i-2])

print(fib)