A1 = int(input("Koeffitsientni kiriting: A1 = "))
B1 = int(input("Koeffitsientni kiriting: B1 = "))
C1 = int(input("Koeffitsientni kiriting: C1 = "))
A2 = int(input("Koeffitsientni kiriting: A2 = "))
B2 = int(input("Koeffitsientni kiriting: B2 = "))
C2 = int(input("Koeffitsientni kiriting: C2 = "))

D = (A1*B2 - A1*B1)
x = (C1*B2-C2*B1)/D
y = (A1*C2-A2*C1)/D

print("A1 * x + B1 * y = C1",
      "\nA2 * x + B2 * y = C2",
      "\nx = {} y = {}".format(x,y))