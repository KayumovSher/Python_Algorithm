def SortInc3(a,b,c):
    if a<b:
        a,b=b,a
    if a<c:
        a,c=c,a
    if b<c:
        b,c=c,b
    return a,b,c

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(SortInc3(a,b,c))