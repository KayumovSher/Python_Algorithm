# 1:22

def ShiftRight3(A,B,C):
    D=A
    E=B
    F=C

    A=F
    B=D
    C=E
    return A,B,C


A1 = int(input("A1 = "))
B1 = int(input("B1 = "))
C1 = int(input("C1 = "))
A1,B1,C1=ShiftRight3(A1, B1, C1)
print(f"A1 = {A1}, B1 = {B1}, C1 = {C1}")

A2 = int(input("A2 = "))
B2 = int(input("B2 = "))
C2 = int(input("C2 = "))
A2,B2,C2=ShiftRight3(A2, B2, C2)
print(f"A2 = {A2}, B2 = {B2}, C2 = {C2}")