# 1:22
def SortInc3(a,b,c):
    if c<a:
        c,a=a,c
    if c<b:
        c,b=b,c
    if b<a:
        b,a=a,b
    return a,b,c

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(SortInc3(a,b,c))