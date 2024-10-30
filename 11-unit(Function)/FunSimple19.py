# from math import abs

def RingS(R):
    PI = 3.1415
    S = PI*(R**2)
    return S

R1 = int(input("R1 = "))
R2 = int(input("R2 = "))

Radius1 = RingS(R1); Radius2 = RingS(R2)

KesishmaydiR = abs(Radius1-Radius2)

print(f"Kiritilgan Radiuslar: {R1}, {R2} ularning yuzalari {Radius1}, {Radius2} va ularning kesishmaydigan yuzasi {KesishmaydiR}")
