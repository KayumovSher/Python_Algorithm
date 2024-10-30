# S = 1+1/2+1/3+.....+1/n

n = int(input("n = "))

S = 0

if n > 0:
    for i in range(1, n+1):
        S += 1 / i
    print("The sum of the harmonic series (S) up to {} terms is: {:.3f}".format(n, S))
else:
    print("Value error") 
    



