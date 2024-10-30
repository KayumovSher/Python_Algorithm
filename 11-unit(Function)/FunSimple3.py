from math import sqrt

def MEAN(X, Y):
    intermediate_arithmetic = (X + Y)/2
    intermediate_geometric = sqrt(X*Y)
    return intermediate_arithmetic, intermediate_geometric

A = float(input("Enter a value of A = "))
B = float(input("Enter a value of B = "))
C = float(input("Enter a value of C = "))
D = float(input("Enter a value of D = "))

result1, result1_2 = MEAN(A, B)
result2, result2_2 = MEAN(A, C)
result3, result3_2 = MEAN(A, D)

print(f"Intermediate Arithmetic and Intermediate Geometric of {A} and {B} are {result1}, {result1_2}")
print(f"Intermediate Arithmetic and Intermediate Geometric of {A} and {C} are {result2}, {result2_2}")
print(f"Intermediate Arithmetic and Intermediate Geometric of {A} and {D} are {result3}, {result3_2}")