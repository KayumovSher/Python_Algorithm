# Define IsPrime(N) the given numbers prime or not
def IsPrime(N):
    for i in range(1, N+1):
        s = 0
        for j in range(1, N+1):
            if i%j == 0:
                s += 1
        if s == 2:
            return print(True)    
        elif s > 2:
            return print(False)
        

k = int(input("How many times do you want to enter numbers to find the prime numbers: "))

for i in range(1, k+1):
    n = int(input("Enter a number: "))
    while n<=0:
        print("N must be greater than 0. Please, enter valid value!")
        n = int(input("Enter a number: "))
    result = IsPrime(n)
