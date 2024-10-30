# 2 sonning EKUB ini topishning optimal usuli

a = int(input('a = '))
b = int(input('b = '))

while a!=b:
    if a>b:
        a%=b
    else:
        b%=a
    if a==0:
        a=b
    if b==0:
        a=b
print(a, b)     