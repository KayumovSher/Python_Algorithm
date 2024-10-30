n = int(input("Istalgan butun juft n sonini kiriting = "))
while not n%2==0:
    print("Kiritgan soningiz juft bo'lishi kerak. Iltimos qaytadan urinib ko'ring.")
    n = int(input("Istalgan butun juft n sonini kiriting = "))

A = []

for i in range(n):
    A.append(int(input("A = ")))

print(A[0],A[2],A[4])