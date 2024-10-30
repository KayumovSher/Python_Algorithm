A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

def Swap(x, y):
    A=y
    B=x    
    return A,B

qiymat1, qiymat2 = Swap(A, B)
qiymat3, qiymat4 = Swap(C, D)

print(f"A={qiymat1}\nB={qiymat2}\nC={qiymat3}\nD={qiymat4}")