# Degrees × (π/180) = Radians

from math import pi

a = int(input("å - burchak gradusda berilgan (0° < å < 360°) -> "))

while not 0<a<=360:
    print("Kiritilgan burchak gradusi 0dan katta va 360 dan kichik bo'lishi kerak.\nIltimos qaytadan urinib ko'ring!")
    a = int(input("a - burchak gradusda berilgan (0° < å < 360°) -> "))

rad = a*(pi/180)

print(f"Kiritilgan gradus å = {a} va uning radiani rad = {rad}")
