def RectPS(x1, y1, x2, y2):
    A = x2-x1
    B = y2-y1
    P = 2*(A+B)
    S = A*B
    return A, B, P, S

X1 = int(input("X1 = "))
Y1 = int(input("Y1 = "))

X2 = int(input("X2 = "))
Y2 = int(input("Y2 = "))

A, B, P, S = RectPS(X1, Y1, X2, Y2)

print(f"To'g'ri to'rtburchakning\nTomonlari: A = {A}, B = {B}\nPerimetri = {P}, Yuzasi = {S}")