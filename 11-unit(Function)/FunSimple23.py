def Quarter(X, Y)
    

    
    if X>0 and Y>0:
        return f"{X} va {Y} o'qi 1-chorakda"
    if X<0 and Y>0:
        return f"{X} va {Y} o'qi 2-chorakda"
    if X<0 and Y<0:
        return f"{X} va {Y} o'qi 3-chorakda"
    if X>0 and Y<0:
        return f"{X} va {Y} o'qi 4-chorakda"

X,Y=Quarter(X,Y)
X = int(input("Koordinataning X o'qini kiriting -> "))
Y = int(input("Koordinataning Y o'qini kiriting -> "))

while X==0 or Y==0:
    print("Koordinata belgilangan nuqtalar 0 bo'lmasligi lozim, Iltimos qaytadan urinib ko'ring.")
    X = int(input("Koordinataning X o'qini kiriting -> "))
    Y = int(input("Koordinataning Y o'qini kiriting -> "))