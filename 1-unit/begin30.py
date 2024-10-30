from math import pi

a = int(input("a burchak radianda berilgan (0 < ∂ < 2π)"))
while not 0<a<=360:
    print("Kiritilgan burchak radiani 0dan katta va 360 dan kichik bo'lishi kerak.\nIltimos qaytadan urinib ko'ring!")
    a = int(input("a - burchak gradusda berilgan (0° < å < 360°) -> "))

degree = a * (180/pi)

print(f"Kiritilgan radian = {a} va uning gradusi = {degree}")