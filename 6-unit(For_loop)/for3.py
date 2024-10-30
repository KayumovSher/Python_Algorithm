a = int(input("a = "))
b = int(input("b = "))

if a < b:
    for i in range(b-1, a, -1):
        print(i)