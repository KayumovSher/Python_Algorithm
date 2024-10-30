def STriangle(R):
    PI=3.1415
    S=PI*(R**2)
    return S

R1 = int(input("R1 = "))
R2 = int(input("R2 = "))

print(f"Kiritilgan Doiraning Radiusi = {R1} va uning yuzasi S = {STriangle(R1)}")
print(f"Kiritilgan ikkinchi Doiraning Radiusi = {R2} va uning yuzasi S = {STriangle(R2)}")
