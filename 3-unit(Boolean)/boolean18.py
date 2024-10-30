a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# print(a == b or b == c or a == c , a != b or b != c)

if a == b or b == c or a == c:
    print(True)
    
elif a == b and b == c and a == c:
    print(False)