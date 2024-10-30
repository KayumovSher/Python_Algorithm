A = int(input("Enter point A on the number line -> "))
B = int(input("Enter point B on the number line -> "))
C = int(input("Enter point C on the number line -> "))


if A < B or A < C:
    if B - A < C - A:
        print("The closest point to point A is this B.")
        print(f"Given points. A = {A}, B = {B} and the between surface is {B-A}.")
    elif B - A > C - A:
        print("The closest point to point A is this C.")
        print(f"Given points. A = {A}, C = {C} and the between surface is {C-A}.")
    elif B == C:
        print("Both B and C elements are the same value and both the closest point to point A")
        print(f"Given points. A = {A}, B = {B}, C = {C} and the between surface is {B-A}")

elif A > B or A > C:
    if A - B < A - C:
        print("The closest point to point A is this B.")
        print(f"Given points. A = {A}, B = {B} and the between surface is {A-B}.")
    elif A - B > A - C:
        print("The closest point to point A is this C.")
        print(f"Given points. A = {A}, C = {C} and the between surface is {A-C}.")
    elif B == C:
        print("Both B and C elements are the same value and both the closest point to point A")
        print(f"Given points. A = {A}, B = {B}, C = {C} and the between surface is {A-B}")

else:
    while A==B==C:
        print("Invalid value! All points must not be same, Please enter other points.")
        A = int(input("Enter point A on the number line -> "))
        B = int(input("Enter point B on the number line -> "))
        C = int(input("Enter point C on the number line -> "))