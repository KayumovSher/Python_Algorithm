def Minmax(x, y):
    if x>y:
        x,y=y,x
    return x,y

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

a,b = Minmax(a,b)
c,d = Minmax(c,d)
a,c = Minmax(a,c)
b,d = Minmax(b,d)

print(a,d)